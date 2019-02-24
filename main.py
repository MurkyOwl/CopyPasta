import wx, keyboard, requests, json, gui, wx.adv, sys, traceback




class CopyFrame(gui.Mainframe):
	#Constructor thingie
	def __init__(self, parent):
		#Calling the MAINFRAME!!!! IE starting the GUI section
		gui.Mainframe.__init__(self,parent)
		#below here we have the trigger action, problem so far is that when you set it to trigger on release True, it doesnt work, self.copier starts the copier function. 
		keyboard.add_hotkey('ctrl+c', self.copier, suppress=False, timeout=1, trigger_on_release=False)

	#Copier function grabs the code from clipboard then runs it through the gauntlet 
	def copier(self):
		# setting a appropriate object to put the clipboard stuff into, 
		text_data = wx.TextDataObject()
		#opening and grabbing the clipboard stuff, 
		if wx.TheClipboard.Open():
			success = wx.TheClipboard.GetData(text_data)
		#if we are successful we send the contents of the clipboard to Evepraisal for appraisal
		if success:
			payload = text_data.GetText()
			header= {'user-agent': 'Atrol Nalelmir, Triumvirate, Ganking Helper'}
			r = requests.post('https://evepraisal.com/appraisal.json?market=jita', data=payload, headers=header)

			#put our return content into a dict
			data = json.loads(r.content)

			# and finally below we look through the return content if its bad we show that it is not an eve copy, if its good we edit the appropriate places with the right response!
			if data.get("error_title") == "Invalid input":
				self.sellValue.Clear()
				self.sellValue.AppendText("Not an Eve copy")
			else:
				webID = data.get("appraisal").get("id")
				sellValue = data.get("appraisal").get("totals").get("sell")
				buyValue = data.get("appraisal").get("totals").get("buy")
				volume = data.get("appraisal").get("totals").get("volume")

				self.sellValue.Clear()
				self.buyValue.Clear()
				self.Volume.Clear()

				self.m_hyperlink1.SetURL('https://evepraisal.com/a/{}'.format(webID))
				if sellValue < 1000000:
					self.sellValue.AppendText("{0:,.2f} THOUSAND".format(sellValue))
				elif sellValue < 1000000000:
					self.sellValue.AppendText("{0:,.2f} MILLION".format(sellValue))
				elif sellValue < 1000000000000:
					self.sellValue.AppendText("{0:,.2f} Billion".format(sellValue))
				else:
					self.sellValue.AppendText("{0:,.2f} KILL IT NOW!".format(sellValue))


				if buyValue < 1000000:
					self.buyValue.AppendText("{0:,.2f} THOUSAND".format(buyValue))
				elif buyValue < 1000000000:
					self.buyValue.AppendText("{0:,.2f} MILLION".format(buyValue))
				elif buyValue < 1000000000000:
					self.buyValue.AppendText("{0:,.2f} Billion".format(buyValue))
				else:
					self.buyValue.AppendText("{0:,.2f} KILL IT NOW!".format(buyValue))

				self.Volume.AppendText("{0:,.2f}".format(volume))
				sellValue = None
				buyValue = None
				volume = None








#Starting application shit
def main():
	app = wx.App(redirect=True,filename="pastalog.txt")
	frame = CopyFrame(None)
	frame.Show(True)
	app.MainLoop()
	
if __name__ == '__main__':
	main()

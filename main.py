import wx, keyboard, requests, json, gui, wx.adv

class CopyFrame(gui.Mainframe):
    #Constructor thingie
    def __init__(self, parent):
        #Calling the MAINFRAME!!!!
        gui.Mainframe.__init__(self,parent)
        keyboard.add_hotkey('ctrl+c', self.copier, suppress=False, timeout=1, trigger_on_release=False)


    #Copier function grabs the code from clipboard then runs it through the gauntlet 
    def copier(self):

        text_data = wx.TextDataObject()
        if wx.TheClipboard.Open():
            success = wx.TheClipboard.GetData(text_data)
        if success:
            payload = text_data.GetText()
            header= {'user-agent': 'Atrol Nalelmir, Triumvirate, Ganking Helper'}
            r = requests.post('https://evepraisal.com/appraisal.json?market=jita', data=payload, headers=header)

            
            data = json.loads(r.content)

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
                self.sellValue.AppendText("{0:,.2f}".format(sellValue))
                self.buyValue.AppendText("{0:,.2f}".format(buyValue))
                self.Volume.AppendText("{0:,.2f}".format(volume))
                sellValue = None
                buyValue = None
                volume = None








#Starting application shit
app = wx.App(False)
frame = CopyFrame(None)
frame.Show(True)
app.MainLoop()

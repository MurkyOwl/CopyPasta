# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version May 29 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv

###########################################################################
## Class Mainframe
###########################################################################

class Mainframe ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Copypasta", pos = wx.DefaultPosition, size = wx.Size( 355,301 ), style = wx.DEFAULT_FRAME_STYLE|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer1 = wx.GridSizer( 4, 2, 5, 5 )
		
		self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Evepraisal Link:", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		gSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.m_hyperlink1 = wx.adv.HyperlinkCtrl( self.m_panel1, wx.ID_ANY, u"Click Me,", wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE )
		gSizer1.Add( self.m_hyperlink1, 0, wx.ALL, 5 )
		
		self.statictext3 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Sell Value:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.statictext3.Wrap( -1 )
		gSizer1.Add( self.statictext3, 0, wx.ALL, 5 )
		
		self.sellValue = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), wx.TE_CHARWRAP|wx.TE_LEFT|wx.TE_READONLY )
		gSizer1.Add( self.sellValue, 0, wx.ALL, 5 )
		
		self.statictext5 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Buy value", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.statictext5.Wrap( -1 )
		gSizer1.Add( self.statictext5, 0, wx.ALL, 5 )
		
		self.buyValue = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), wx.TE_CHARWRAP|wx.TE_LEFT|wx.TE_NO_VSCROLL|wx.TE_READONLY )
		gSizer1.Add( self.buyValue, 0, wx.ALL, 5 )
		
		self.m_staticText7 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Volume:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		gSizer1.Add( self.m_staticText7, 0, wx.ALL, 5 )
		
		self.Volume = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), wx.TE_CHARWRAP|wx.TE_LEFT|wx.TE_READONLY )
		gSizer1.Add( self.Volume, 0, wx.ALL, 5 )
		
		
		self.m_panel1.SetSizer( gSizer1 )
		self.m_panel1.Layout()
		gSizer1.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	


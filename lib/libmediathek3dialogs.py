# -*- coding: utf-8 -*-
import urllib
import urllib2
import socket
import sys
import xbmc
import xbmcplugin
import xbmcgui
import xbmcaddon
import xbmcvfs
import re
from datetime import datetime
import time

import libmediathek3utils

def dialogDate(format='%d%m%Y'):
	dialog = xbmcgui.Dialog()
	result = dialog.numeric(1, libmediathek3utils.getTranslation(31030)).replace("/", "").replace(" ", "0")
	try:
		result = datetime.strptime(result, '%d%m%Y')
	except TypeError:  # handle bug in Python 2
		result = datetime(*(time.strptime(result, '%d%m%Y')[0:6]))
	return result.strftime(format)
	
def getSearchString():
	dialog = xbmcgui.Dialog()
	d = dialog.input(libmediathek3utils.getTranslation(31039),type=xbmcgui.INPUT_ALPHANUM)
	return urllib.quote_plus(d)

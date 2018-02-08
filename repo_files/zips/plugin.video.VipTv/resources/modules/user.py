import base64 as b
import xbmcaddon
id   = b.b64decode('cGx1Z2luLnZpZGVvLlZpcFR2')

name = b.b64decode('VmlwIFR2')

port = b.b64decode('ODA=')

def host():
	if xbmcaddon.Addon().getSetting('direct') == 'true':
		url = b.b64decode('aHR0cDovL3ZpcHR2LnpvbmU=')
	else:
		url = b.b64decode('aHR0cDovL2Vhc3kudmlwdHYuem9uZQ==')
	return url
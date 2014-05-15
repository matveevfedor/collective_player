from mpd import MPDClient
from string import *
import json

def list_tracks():
	client = MPDClient()
	client.connect("localhost",6600)
	response = client.lsinfo()
	client.close()
	client.disconnect()
	return json.dumps(response, indent=4,separators=(',',':'))	
	



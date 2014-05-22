from mpd import MPDClient
import json

def find_track(mode, key):
	client = MPDClient()
	client.connect("localhost",6600)
	response = client.find(mode,key)
	client.close()
	client.disconnect()
	return json.dumps(response)

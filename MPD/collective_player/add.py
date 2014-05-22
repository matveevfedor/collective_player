from mpd import MPDClient
import json

def add_track(name_track):
	client = MPDClient()
	client.connect("localhost",6600)
	response = client.addid(name_track)
	client.close()
	client.disconnect()
	return json.dumps(response)

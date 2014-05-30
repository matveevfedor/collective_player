from mpd import MPDClient
import json

def update_queue(current_queue):
	client = MPDClient()
	client.connect("localhost", 6600)
	response = client.playlistinfo()
	client.close()
	client.disconnect()
	return json.dumps(response)

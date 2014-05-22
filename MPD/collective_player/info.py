import json
from mpd import MPDClient
def get_info(track_pos):
	client = MPDClient()
	client.connect("localhost",6600)
	response = client.playlistinfo(track_pos)
	client.close()
	client.disconnect()
	return json.dumps(response)

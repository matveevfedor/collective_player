from mpd import MPDClient
def get_info(track_pos):
	client = MPDClient()
	client.connect("localhost",6600)
	response = client.playlistifo(track_pos)
	cleint.close()
	client.disconnect()
	return json.dumps(response)

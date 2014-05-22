from mpd import MPDClient

def play_queue():
	client = MPDClient()
	client.connect("localhost", 6600)
	response = client.play(0)
	client.close()
	client.disconnect()
	return true

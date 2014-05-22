from mpd import MPDClient

def play_queue():
	client = MPDClient()
	client.connect("localhost", 6600)
	response = client.play(1)
	response = client.delete(0)
	client.close()
	client.disconnect()
	return True

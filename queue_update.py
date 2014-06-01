# -*- coding: utf-8 -*-
#Collective_player_server
#Модуль получения текущей очереди воспроизведения
from mpd import MPDClient
import json
#Функция update_queue - обновляет текущую очередь воспроизведения
#Проверяется состояние проигрывателя
#Если очередь проигрывается, то удаляются все трека предшествующие текущему
#Возвращаемое значение - текущая очередь в формате JSON
def update_queue():
	client = MPDClient()
	client.connect("localhost", 6600)
	status = client.status()
	if status['state'] == 'play':
		current_song = client.currentsong()
		current_song_position = current_song['pos']
		if int(current_song_position) > 0:
			client.delete('0:'+current_song_position)	
	try:
		response = json.dumps(client.playlistinfo())
	except:
		response = False
	client.close()
	client.disconnect()
	return response

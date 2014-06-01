# -*- coding: utf-8 -*-
#Collective_player_server
#Модуль получения списка всех треков
from mpd import MPDClient
import json
#Функция list_tracks - получение списка треков от MPD сервера
#Возвращаемое значение - список треков в формате JSON
def list_tracks():
	client = MPDClient()
	client.connect("localhost",6600)
	try:
		response = json.dumps(client.lsinfo())
	except:
		response = False	
	client.close()
	client.disconnect()
	return response	
	



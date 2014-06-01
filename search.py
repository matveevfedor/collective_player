# -*- coding: utf-8 -*-
#Collective_player_server
#Модуль поиска по списку треков
from mpd import MPDClient
import json
#Функция find_track - оуществляет поиск по списку треков
#@param mode - способ поиска
#@param key - ключ поиска
#Возвращаемое значение - информация о найденном треке или пустой массив
def find_track(mode, key):
	client = MPDClient()
	client.connect("localhost",6600) 
	try:
		response = json.dumps(client.find(mode,key))
	except:
		response = False
	client.close()
	client.disconnect()
	return response

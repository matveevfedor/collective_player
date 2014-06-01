# -*- coding: utf-8 -*-
#Collective_player_server
#Модуль получения информации о треке
import json
from mpd import MPDClient
#Функция get_info - осуществляет получение информации о трке от MPD сервера
#@param track_pos - позиция трека в очереди воспроизведения
#@return_value - response - информация о треке в JSON
def get_info(track_pos):
	client = MPDClient()
	client.connect("localhost",6600)
	if int(track_pos) < 0:
		response =  False
	else:
		try:
			response = json.dumps(client.playlistinfo(track_pos))
		except:
			response = False
	client.close()
	client.disconnect()
	return response

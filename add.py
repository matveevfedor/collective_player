# -*- coding: utf-8 -*-
#Collective_player_server
#Модуль добавления трека в очередь
from mpd import MPDClient
import json
#Функция add_track - осуществляет добавление трека в очередь воспроизведения
#@params: name - имя добавляемого в очередь файла
#return value - response - boolean (успех или неудача добавления файла)
def add_track(name):
	client = MPDClient()
	client.connect("localhost",6600)
	try:
		client.addid(name)
		response = True
	except:	
		response = False
	client.close()
	client.disconnect()
	return response

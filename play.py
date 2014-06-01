# -*- coding: utf-8 -*-
#Collective_player_server
#Модуль запуска воспроизведения очереди
from mpd import MPDClient
import json
#Функция play_queue - осуществляет запуск очереди воспроизведения
#возвращаемое значение result - успех/неудача
def play_queue():
	client = MPDClient()
	client.connect("localhost", 6600)
	try:
		result = json.dumps(client.play(0))
	except:	
		result = False	
	client.close()
	client.disconnect()
	return result

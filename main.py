# -*- coding: utf-8 -*-
#Collective_player_server
# Основной модуль сервера
# Осуществляет взаимодействие с клиентскими приложениями
from bottle import run, route, post, template, request,response,HTTPResponse
from list import list_tracks
from search import find_track
from queue_update import update_queue
from info import get_info
from play import play_queue
from add import add_track
import datetime

#Текущая очереди воспроизведения
_current_queue = []
#Обработка запроса от клиента на получение текущей очереди воспроизведения
#Отправляется текущая очередь в формате JSON
#Либо HTTP код 304-Not-Modified, если очередь не обновлялась с момента последнего обращения
@route('/queue')
def get_queue():
	global _current_queue
	new_queue = update_queue()
	if new_queue:
		if new_queue == _current_queue:
			return HTTPResponse(status=304)
		else:
			_current_queue = new_queue
			updating = datetime.datetime.utcnow().ctime()
			response.set_header('Content-type', 'application/json')
			response.set_header('Last-Modified', updating)
			return _current_queue
	else:
		return HTTPResponse(status=500)
#Обработка запроса от клиента на получение списка всех треков
@route('/tracks/all')
def get_tracks():
	response.set_header('Content-type','application/json')
	result = list_tracks()
	if result:
		return result
	else:
		return HTTPResponse(status=500)
#Обработка POST-запроса от клиента на добавление трека в очередь
#Принимается параметр name - имя добавляемого в очередь трека
@post('/queue')
def add():
	name = request.forms.get('name')
	result =  add_track(name)
	if result:
		return get_queue()
	else:
		return HTTPResponse(status=500)
#Обработка GET-запроса от клиента на осуществление поиска по трекам
#Принимаеюся запросы вида /tracks?mode=''&what=''
#mode - способ поиска
#what - искомый трек
@route('/tracks')
def find():
	mode = request.query.mode
	what = request.query.what
	response.set_header('Content-type', 'application/json')
	result = find_track(mode, what)
	if result:
		return result
	else:
		return HTTPResponse(status=500)
#Обработка запроса от клиента на получение информации по конкретному треку
#Обрабатывается GET-запрос вида /queue/<pos>
#<pos> - позиция трека в очередь
#В случае неверно заданной или несуществующей позиции трека
#будет возвращен 404 HTTP код
@route('/queue/<pos>')
def info(pos):
	result = get_info(pos)
	response.set_header('Content-type', 'application/json')
	if result:
		return get_info(pos)
	else:
		return HTTPResponse(status=404)
#Обработка запроса от клиента на воспроизведение текущей очереди
@route('/queue/play/')
def play():
	result = play_queue()
	if result:
		return 'playing'
	else:
		return HTTPResponse(status=500)
#Запуск сервера, установка прослушиваемого порта
run(host='0.0.0.0', port=8080, debug='false')

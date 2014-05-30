
from bottle import run, route, post, template, request, BaseResponse
from list import list_tracks
from search import find_track
from queue_update import update_queue
from info import get_info
from play import play_queue

_current_queue = []
@route('/queue')
def get_queue():
	global _current_queue
	new_queue = update_queue(_current_queue)
	if new_queue == _current_queue:
		return BaseResponse(status_code=304)
	else:
		_current_queue = new_queue
		return _current_queue

@route('/tracks/all')
def get_tracks():
	r = list_tracks()
	return  r

@post('/queue/add')
def add():
	return "hello"

@route('/tracks')
def find():
	mode = request.query.mode
	what = request.query.what
	return find_track(mode, what)

@route('/queue/<pos>')
def info(pos):
	return get_info(pos)
@route('/queue/play/')
def play():
	play_queue()
	return 'playing'


run(host='0.0.0.0', port=8080, debug='false')

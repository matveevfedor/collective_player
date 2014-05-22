from bottle import run, route, post, template, request
from list import list_tracks
from search import find_track
from queue_update import update_queue

@route('/queue')
def get_queue():
	return update_queue().replace('\n','<br/>')

@route('/tracks/all')
def get_tracks():
	r = list_tracks().replace('\n','<br/>')
	return  r

@post('/queue/add')
def add():
	return "hello"

@route('/tracks')
def find():
	mode = request.query.mode
	what = request.query.what
	return find_track(mode, what)

@route('/tracks/<pos>')
def info(pos):
	return pos

run(host='0.0.0.0', port=8080, debug='false')

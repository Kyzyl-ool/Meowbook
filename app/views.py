from flask import request, abort, jsonify
from app import app
from .model import *




CHATS_LIST = ['Meow', 'Gaw', 'Gavgav', 'Muu']
CONTACTS_LIST = ['Cat', 'Dog', 'Mouse', 'Kitty', 'Cow', 'Bird']


@app.route('/<string:name>/')
@app.route('/')
def index(name = "World"):
	return "Hello, {}!".format(name)


@app.route('/form/', methods = ['POST', 'GET'])
def form():
	if request.method == 'GET':
		return """<html><head></head><body>
		<form method = "POST" action = "/form/">
			<input name = "first_name">
			<input name = "last_name">
			<input type = "submit">
		</form></body></html>"""
	else:
		rv = jsonify(request.form)
		return rv

@app.route('/chats/', methods = ['GET'])
def get_chats_list():
	result = {}
	result['status_code'] = '200 OK'
	result['mimetype'] = 'application/json'
	result['chats'] = CHATS_LIST
	return jsonify(result)

@app.route('/contacts/', methods = ['GET'])
def get_contacts_list():
	result = {}
	result['status_code'] = '200 OK'
	result['mimetype'] = 'application/json'
	result['contacts'] = CONTACTS_LIST
	return jsonify(result)


@app.route('/new_chat/', methods = ['GET', 'POST'])
def create_new_chat():
	if request.method == 'GET':
		return """<html><head></head><body>
		<form method = "POST" action = "/new_chat/">
			<input name = "chat_name">
			<input type = "submit">
		</form></body></html>"""
	else:
		CHATS_LIST.append(request.form['chat_name'])
		return jsonify(request.form)

@app.route('/users/')
def users():
	users_list = get_users_list_by_mask('asd')
	return jsonify(list(map(dict, users_list))[0])

from flask import request, abort, jsonify, Response
from app import app
from .model import *




# CHATS_LIST = ['Meow', 'Gaw', 'Gavgav', 'Muu']
# CONTACTS_LIST = ['Cat', 'Dog', 'Mouse', 'Kitty', 'Cow', 'Bird']


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

# @app.route('/chats/', methods = ['GET'])
# def get_chats_list():
# 	result = {}
# 	result['status_code'] = '200 OK'
# 	result['mimetype'] = 'application/json'
# 	result['chats'] = CHATS_LIST
# 	return jsonify(result)


@app.route('/new_chat/', methods = ['GET', 'POST'])
def create_new_chat():
	if request.method == 'GET':
		return """<html><head></head><body>
		<form method = "POST" action = "/new_chat/">
			<input name = "chat_topic">
			<p><input name = "is_group_chat" type="checkbox" value = "True">Групповой чат</p>
			<input type = "submit" placeholder="Имя чата">
		</form></body></html>"""
	else:
		# print(request.form['is_group_chat'])
		# add_new_chat(1, request.form['is_group_chat'], request.form['chat_topic'], 0)
		# CHATS_LIST.append(request.form['chat_name'])
		request_form_data = dict(request.form)
		request_form_data['chat_topic'] = request_form_data['chat_topic'][0]

		if 'is_group_chat' not in request_form_data:
			request_form_data['is_group_chat'] = False
		else:
			request_form_data['is_group_chat'] = True

		add_new_chat(request_form_data['is_group_chat'], request_form_data['chat_topic'], 0)

		return jsonify(request_form_data)

@app.route('/users/')
def users():
	mask = request.args.get('mask')
	if mask == None: mask = '%'
	return jsonify(get_users_list_by_mask(mask))

@app.route('/chats_list/')
def chats():
	return jsonify(get_chats_list())
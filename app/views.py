from flask import request, abort, jsonify, redirect
from app import app, jsonrpc
from .model import *
import json
import time
import requests
import base64
import boto3
import config

from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper

boto3_session = boto3.session.Session()
s3_client = boto3_session.client(
	service_name='s3',
	endpoint_url='http://hb.bizmrg.com',
	aws_access_key_id=config.AWS_ACCESS_KEY_ID,
	aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY)


def isNone(var):
	return var is None

def isString(var):
	return isinstance(var, str)

def isInt(var):
	return isinstance(var, int)

def isBool(var):
	return isinstance(var, bool)

@jsonrpc.method('new_chat')
def new_chat(topic, is_group):
	if (
		not isNone(topic) and not isNone(is_group) and
		isString(topic) and isBool(is_group)
		):
		add_new_chat(is_group, topic, 0)
		return {'code': 200}
	else:
		return {'code': 400}


@jsonrpc.method('new_message')
def new_message(chat_id, user_id, content):
	if (
		not isNone(chat_id) and not isNone(user_id) and not isNone(content) and
		isInt(chat_id) and isInt(user_id) and isString(content)
		):
		add_new_message(chat_id, user_id, content, time.strftime('%Y-%m-%d %H:%M:%S'))
		return {'code': 200}
	else:
		return {'code': 400}

@jsonrpc.method('get_users')
def get_users(mask):
	if (not isNone(mask) and isString(mask)):
		return jsonify(get_users_list_by_mask(mask)).json
	else:
		return {'code': 400}

@jsonrpc.method('get_chats')
def get_chats(user_id):
	print('user id: ',user_id)
	return jsonify(get_members_list(user_id)).json

@jsonrpc.method('get_messages')
def get_message(chat_id, user_id):
	if (not isNone(chat_id) and not isNone(user_id) and
		isInt(chat_id) and isInt(user_id)
		):
		return jsonify(get_messages(chat_id, user_id)).json
	else:
		return {'code': 400}

@app.route('/get_first_token/')
def get_first_token():
	return redirect('https://oauth.vk.com/authorize?client_id=6763334&redirect_uri=http://127.0.0.1:3000/authpage/&v=5.92&display=page&response_type=code&scope=1')


@jsonrpc.method('get_access_token')
def auth(code):
	print(code)
	access_token_url = 'https://oauth.vk.com/access_token?client_id=6763334&client_secret=UkX5Gbkg2pJdK9PfHunI&redirect_uri=http://127.0.0.1:3000/authpage/&code={}'.format(code)
	resp = requests.get(access_token_url)
	print(resp.text)
	return resp.text
	# json_data = json.loads(resp.text)
	# return json_data

@jsonrpc.method('get_user_data')
def get_user_data(access_token, user_id):
	user_data_url = 'https://api.vk.com/method/users.get?user_ids={}&access_token={}&v=5.92'.format(user_id, access_token)
	resp = requests.get(user_data_url)
	return resp.text

@jsonrpc.method('upload_file')
def upload_file(base64content, filename):
	if (s3_client.put_object(
								Bucket='2018-kezhik-kyzyl_ool-bucket',
								Key=filename,
								Body=base64.b64decode(base64content) )):
		return {'code': 200}
	else:
		return {'code': 500, 'error': 'Error with s3 client.'}

@jsonrpc.method('download_file')
def download_file(filename):
	return s3_client.get_object(Bucket='2018-kezhik-kyzyl_ool-bucket', Key=filename).get('Body').read().decode('utf-8')
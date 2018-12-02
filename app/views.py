from flask import request, abort, jsonify, redirect
from app import app, jsonrpc, s3_client, cent_client
from .model import *
from .vk_requests import *
from .checkers import *

import json
import time
import requests
import base64
import jwt
import config

from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper


@jsonrpc.method('new_chat')
def new_chat(topic, is_group):
    if (
            not isNone(topic) and not isNone(is_group) and
            isString(topic) and isString(is_group)
    ):
        return jsonify(add_new_chat(is_group, topic)).json
    else:
        return {'code': 400}


@jsonrpc.method('new_message')
def new_message(chat_id, user_id, content):
    # publish data into channel

    # channel = "public:chat1"
    # data = {"text": content}
    # cent_client.publish(channel, data)

    if (
            not isNone(chat_id) and not isNone(user_id) and not isNone(content) and
            isInt(chat_id) and isInt(user_id) and isString(content)
    ):
        return add_new_message(chat_id, user_id, content, time.strftime('%Y-%m-%d %H:%M:%S'))
    else:
        return {'code': 400}

@jsonrpc.method('new_file_message')
def new_file_message(chat_id, user_id, content, filename, type, size):
    if (
            not isNone(chat_id) and not isNone(user_id) and not isNone(content) and not isNone(filename) and not isNone(type) and not isNone(size) and
            isInt(chat_id) and isInt(user_id) and isString(content) and isString(filename) and isString(type) and isInt(size)
    ):
        return add_new_file_message(chat_id, user_id, content, time.strftime('%Y-%m-%d %H:%M:%S'), filename, type, size)
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
    return jsonify(get_members_list(user_id)).json


@jsonrpc.method('get_messages')
def get_message(chat_id):
    if (not isNone(chat_id) and
            isInt(chat_id)
    ):
        return jsonify(get_messages(chat_id)).json
    else:
        return {'code': 400}


@app.route('/get_first_token/')
def get_first_token_method():
    return get_first_token()


@jsonrpc.method('get_access_token')
def get_access_token_method(code):
    return get_access_token(code)


# json_data = json.loads(resp.text)
# return json_data

@jsonrpc.method('get_user_data')
def get_user_data_method(access_token, user_id):
    return get_user_data(access_token, user_id)


@jsonrpc.method('upload_file')
def upload_file(base64content, filename):
    if (s3_client.put_object(
            Bucket=config.BUCKET_NAME,
            Key=filename,
            Body=base64.b64decode(base64content))):
        return {'code': 200}
    else:
        return {'code': 500, 'error': 'Error with s3 client.'}


@jsonrpc.method('download_file')
def download_file(filename):
    return s3_client.get_object(Bucket=config.BUCKET_NAME, Key=filename).get('Body').read().decode('utf-8')


@jsonrpc.method('get_centrifuge_token')
def get_centrifuge_token():
    return jwt.encode({"sub": "0"}, config.CENTRIFUGO_SECRET).decode()


@jsonrpc.method('add_new_member_to_chat')
def add_new_member_to_chat_method(user_id, chat_id):
    if (not isNone(user_id) and not isNone(chat_id) and
            isInt(user_id) and isInt(chat_id)):
        return add_new_member_to_chat(user_id, chat_id)
    else:
        return {'code': 400}


@jsonrpc.method('check_user')
def check_user_method(user_id):
    if (not isNone(user_id) and isInt(user_id)):
        return jsonify(check_user_existance(user_id)).json
    else:
        return {'code': 400}


@jsonrpc.method('create_user')
def create_user_method(user_id, name, nick):
    if (not isNone(user_id) and isInt(user_id) and
            not isNone(name) and isString(name) and
            not isNone(nick) and isString(nick) and
            user_id > 0):
        return create_user(user_id, name, nick)
    else:
        return {'code': 400}


@jsonrpc.method('user_name_by_id')
def user_name_by_id_method(user_id):
    if (not isNone(user_id) and isInt(user_id)):
        return get_name_by_id(user_id)
    else:
        return {'code': 400}
from flask import request, redirect
import requests

def get_user_data(access_token, user_id):
	user_data_url = 'https://api.vk.com/method/users.get?user_ids={}&access_token={}&v=5.92'.format(user_id, access_token)
	resp = requests.get(user_data_url)
	return resp.text

def get_first_token():
	return redirect('https://oauth.vk.com/authorize?client_id=6763334&redirect_uri=http://127.0.0.1:3000/authpage/&v=5.92&display=page&response_type=code&scope=1')

def get_access_token(code):
	access_token_url = 'https://oauth.vk.com/access_token?client_id=6763334&client_secret=UkX5Gbkg2pJdK9PfHunI&redirect_uri=http://127.0.0.1:3000/authpage/&code={}'.format(code)
	resp = requests.get(access_token_url)
	print(resp.text)
	return resp.text


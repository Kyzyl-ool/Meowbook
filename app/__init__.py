import boto3
import config
from flask import Flask
from flask_jsonrpc import JSONRPC
from flask_cors import CORS
from cent import Client
from werkzeug.contrib.profiler import ProfilerMiddleware

app = Flask(__name__)
CORS(app)
jsonrpc = JSONRPC(app, '/')
# app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[3])


boto3_session = boto3.session.Session()
s3_client = boto3_session.client(
	service_name='s3',
	endpoint_url='http://hb.bizmrg.com',
	aws_access_key_id=config.AWS_ACCESS_KEY_ID,
	aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY)


# initialize client instance.
cent_client = Client(config.CENTRIFUGO_URL, api_key=config.CENTRIFUGO_API_KEY, timeout=1)

from .views import *
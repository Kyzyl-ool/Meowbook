from flask import Flask
from flask_jsonrpc import JSONRPC
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
jsonrpc = JSONRPC(app, '/')

from .views import *
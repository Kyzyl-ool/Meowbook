from flask import request, abort, jsonify, Response
from app import app
from .model import *

@app.route('/')
def index():
	return "Hello."
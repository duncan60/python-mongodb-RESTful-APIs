from flask import Flask
from flask.ext import restful
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://127.0.0.1:12345/bookList'


api = restful.Api(app)
mongo = PyMongo(app)

class Index(restful.Resource):
	def get(self):
		return {'msg': 'hello world!'}

api.add_resource(Index, '/')

from app import books

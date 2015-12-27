from flask import Flask
from flask.ext import restful
from books import BookList

app = Flask(__name__)
api = restful.Api(app)

class HelloWord(restful.Resource):
	def get(self):
		return {'hello': 'word'}

api.add_resource(HelloWord, '/')
api.add_resource(BookList, '/books')

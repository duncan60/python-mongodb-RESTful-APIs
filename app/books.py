from flask import Flask
from flask.ext import restful
from app import api, mongo

class BookList(restful.Resource):
	def get(self):
		return [x for x in mongo.db.bookList.find({}, {'_id': 0})]

	def post(self):
		return {'msg': 'ok'}

api.add_resource(BookList, '/books')


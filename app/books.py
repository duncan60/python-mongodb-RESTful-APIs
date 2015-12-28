from flask import Flask, abort
from flask.ext import restful
from flask.ext.restful import reqparse
from app import app, api, mongo

class BookList(restful.Resource):
	def __init__(self, *args, **kwargs):
 		self.reqparse = reqparse.RequestParser()
        #self.reqparse.add_argument('title', type = str, required = True, help = 'No task title provided', location = 'json')
        self.reqparse.add_argument('description', type = str, default = "", location = 'json')
        super(BookList, self).__init__()

	def get(self):
		return [x for x in mongo.db.bookList.find({}, {'_id': 0})]

	def post(self):
		args = self.parser.parse_args()
		jo = json.loads(args['title'], args['price'])
		print jo
		return {'msg': 'ok'}

api.add_resource(BookList, '/books')
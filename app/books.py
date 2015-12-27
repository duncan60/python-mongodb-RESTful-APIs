from flask import Flask
from flask.ext.restful import Resource

books = [
	{
		'id': 1,
		'name': 'books 1',
		'author': 'author A'
	},
	{
		'id': 2,
		'name': 'books 2',
		'author': 'author B'
	},
	{
		'id': 3,
		'name': 'books 3',
		'author': 'author C'
	},
	{
		'id': 4,
		'name': 'books 4',
		'author': 'author D'
	}
];

class BookList(Resource):
	def get(self):
		return {'books_list': books}

	def post(self):
		return {'msg': 'ok'}


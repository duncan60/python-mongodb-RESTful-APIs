from flask import abort
from flask.ext.restful import Resource, reqparse, marshal_with
from app import app, api, mongo, book_resource_fields
from bson.objectid import ObjectId
from bson.regex import Regex

class Search(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type = str)

    @marshal_with(book_resource_fields, envelope='book_list')
    def get(self):
        args = self.reqparse.parse_args()
        books = mongo.db.bookList.find({'title': Regex(args.title)})

        return [x for x in books]

api.add_resource(Search, '/search' , endpoint = 'search')


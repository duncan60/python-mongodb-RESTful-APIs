from flask import abort
from flask.ext.restful import Resource, reqparse, marshal_with
from app import app, api, mongo, resource_fields
from bson.objectid import ObjectId
from bson.regex import Regex

class Search(Resource):
    @marshal_with(resource_fields, envelope='book_list')
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type = str)
        args = parser.parse_args()
        books = mongo.db.bookList.find({'title': Regex(args.title)})
        return [x for x in books]

api.add_resource(Search, '/search' , endpoint = 'search')


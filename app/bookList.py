from flask import abort
from flask.ext.restful import Resource, reqparse, marshal_with
from app import app, api, mongo, resource_fields

class BookList(Resource):
    @marshal_with(resource_fields, envelope='bool_list')
    def get(self):
        return [x for x in mongo.db.bookList.find()]

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type = str, required = True, help = 'No task title provided')
        parser.add_argument('price', type = str, required = True, help = 'No task price provided')
        args = parser.parse_args()
        mongo.db.bookList.insert(args)
        return {'msg': 'create book ok'}, 200

api.add_resource(BookList, '/books', endpoint = 'books')
from flask import abort
from flask.ext.restful import Resource, reqparse, marshal_with
from app import app, api, mongo, book_resource_fields
from bson.objectid import ObjectId
from datetime import datetime

class Book(Resource):
    @marshal_with(book_resource_fields, envelope='book')
    def get(self, book_id):
        book = mongo.db.bookList.find_one_or_404({'_id': book_id})
        return book, 200

    def delete(self, book_id):
        mongo.db.bookList.find_one_or_404({"_id": book_id})
        mongo.db.bookList.delete_one({'_id': book_id})
        return {'msg': 'delete success'}, 200

    def put(self, book_id):
        parser = reqparse.RequestParser()
        parser.add_argument('price', type = str)
        parser.add_argument('title', type = str)
        args = {}

        for k, v in parser.parse_args().iteritems():
            if v != None:
                args[k] = v

        args['date_updated'] = datetime.utcnow()
        mongo.db.bookList.find_one_and_update({'_id': book_id}, {'$set': args})
        return {'msg': 'update success'}, 201

api.add_resource(Book, '/book/<ObjectId:book_id>', endpoint = 'book')
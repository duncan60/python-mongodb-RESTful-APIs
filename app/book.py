from flask import Flask, abort
from flask.ext.restful import Resource, reqparse, marshal_with
from app import app, api, mongo, resource_fields
from bson.objectid import ObjectId

class Book(Resource):
    @marshal_with(resource_fields, envelope='book')
    def get(self, book_id):
        book = mongo.db.bookList.find_one({'_id': book_id})
        return book

    def delete(self, book_id):
        return {'msg': 'delete'}

    def put(self, book_id):
        parser = reqparse.RequestParser()
        parser.add_argument('price', type = str)
        parser.add_argument('title', type = str)
        args = {}
        for k, v in parser.parse_args().iteritems():
            if v != None:
                args[k] = v
        mongo.db.bookList.find_one_and_update({'_id': book_id}, {'$set': args})
        return {'msg': 'update successed'}

api.add_resource(Book, '/book/<ObjectId:book_id>', endpoint = 'book')
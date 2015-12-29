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
        return {'msg': 'put'}

api.add_resource(Book, '/book/<ObjectId:book_id>', endpoint = 'book')
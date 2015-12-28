import json
from flask import Flask, abort
from flask.ext import restful
from flask.ext.restful import reqparse
from app import app, api, mongo

class BookList(restful.Resource):
    def get(self):
        return [x for x in mongo.db.bookList.find({}, {'_id': 0})]

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type = str)
        parser.add_argument('price', type = str)
        args = parser.parse_args()
        mongo.db.bookList.insert(args)
        #jo = json.loads(args['title'], args['price'])
        return {'msg': 'ok'}

api.add_resource(BookList, '/books')
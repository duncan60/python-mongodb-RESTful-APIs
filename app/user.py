from flask import abort
from flask.ext.restful import Resource, reqparse, marshal_with
from app import app, api, mongo, resource_fields
from bson.objectid import ObjectId
from datetime import datetime

class User(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type = str, required = True, help = 'No task name provided')
        parser.add_argument('password', type = str, required = True, help = 'No password price provided')
        args = parser.parse_args()

        if not args['name'] or not args['password']:
            abort(400)

        return {'msg': 'new user success'}

api.add_resource(User, '/user', endpoint = 'user')
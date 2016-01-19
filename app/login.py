from flask import abort
from flask.ext.restful import Resource, reqparse, marshal_with
from app import app, api, mongo
from bson.objectid import ObjectId
from datetime import datetime

class Login(Resource):
    def get(self):
        return {'msg': 'login sucess'}, 201

api.add_resource(Login, '/login', endpoint = 'login')
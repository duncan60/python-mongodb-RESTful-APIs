from flask import abort
from flask.ext.restful import Resource, reqparse, marshal_with
from flask.ext.login import login_user, UserMixin
from app import app, api, mongo, login_manager
from bson.objectid import ObjectId
from datetime import datetime

class User(UserMixin):
    pass

@login_manager.user_loader
def user_loader(name):
    user = User()
    return user

class Login(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type = str, required = True, help = 'No task name provided')
        parser.add_argument('password', type = str, required = True, help = 'No password price provided')
        args = parser.parse_args()

        if not args['name'] or not args['password']:
            abort(400)

        find_user = [x for x in mongo.db.user.find({'name': args['name'], 'password': args['password']}, {'_id':0, 'date_created': 0})]

        if len(find_user) == 0:
            msg = 'none use'
        else:
            msg = 'has use'
            user = User()
            user.id = args['name']
            login_user(user)

        return {'msg': msg}, 201

api.add_resource(Login, '/login', endpoint = 'login')
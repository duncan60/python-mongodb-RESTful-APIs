from flask import abort
from flask.ext.restful import Resource, reqparse, marshal_with
from flask.ext.login import login_user, UserMixin
from app import app, api, mongo, login_manager
from bson.objectid import ObjectId
from datetime import datetime

class User(UserMixin):
    pass

@login_manager.user_loader
def user_loader(id):
    user = User()
    user.id = id
    return user

@login_manager.unauthorized_handler
def unauthorized():
    return {'msg': 'you need login required'}, 401

class Login(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type = str, help = u'No task name provided')
        self.reqparse.add_argument('password', type = str, help = u'No password price provided')

    def get(self):
        args = self.reqparse.parse_args()

        if not args['name'] or not args['password']:
            abort(400)

        try:
            find_user = [x for x in mongo.db.user.find({'name': args['name'], 'password': args['password']})]
        except:
            return {'msg': 'DB Error'}, 500

        if len(find_user) == 0:
            msg = 'name or passowrd error'
        else:
            msg = 'login success'
            user = User()
            user.id = find_user[0]['_id']
            login_user(user, remember=True)
            mongo.db.user.find_one_and_update(
                {'_id': user.id},
                {'$set': {'date_latest_login':datetime.utcnow()}}
            )

        return {'msg': msg}, 201

api.add_resource(Login, '/login', endpoint = 'login')
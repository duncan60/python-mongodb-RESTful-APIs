from flask import abort
from flask.ext.restful import Resource
from flask.ext.login import logout_user, login_required
from app import app, api

class Logout(Resource):
    @login_required
    def get(self):
        logout_user()
        return {'msg': 'logout success'}, 201

api.add_resource(Logout, '/logout', endpoint = 'logout')
from flask import Flask
from flask.ext import restful
from flask.ext.restful import fields
from flask.ext.pymongo import PyMongo
from flask import make_response
from bson.json_util import dumps

app = Flask(__name__)
#MONGO_URL = 'mongodb://127.0.0.1:12345/bookList'
#MONGO_USERNAME= 'test_user'
#MONGO_PASSWORD = '1234'

MONGO_HOST = 'mongodb://127.0.0.1'
MONGO_PORT = '12345'
MONGO_DBNAME = 'bookList'

#app.config['MONGO_URI'] = MONGO_URL
#app.config['MONGO_USERNAME'] = MONGO_USERNAME
#app.config['MONGO_PASSWORD'] = MONGO_PASSWORD

app.config['MONGO_HOST'] = MONGO_HOST
app.config['MONGO_PORT'] = MONGO_PORT
app.config['MONGO_DBNAME'] = MONGO_DBNAME

mongo = PyMongo(app)

def output_json(obj, code, headers=None):
    resp = make_response(dumps(obj), code)
    resp.headers.extend(headers or {})
    return resp


DEFAULT_REPRESENTATIONS = {'application/json': output_json}

api = restful.Api(app)
api.representations = DEFAULT_REPRESENTATIONS

book_resource_fields = {
    '_id': fields.String,
    'title': fields.String,
    'price': fields.Float,
    'date_created': fields.DateTime(dt_format='iso8601'),
    'date_updated': fields.DateTime(dt_format='iso8601')

}

user_resource_fields = {
    '_id': fields.String,
    'name': fields.String,
    'password': fields.String,
    'date_created': fields.DateTime(dt_format='iso8601'),
    'date_updated': fields.DateTime(dt_format='iso8601')

}

class Index(restful.Resource):
    def get(self):
        return {'msg': 'hello Index!'}

api.add_resource(Index, '/')

from app import books, book, search, users

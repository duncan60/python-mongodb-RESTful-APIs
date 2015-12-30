from flask.ext.restful import Resource, reqparse, marshal_with, abort
from app import app, api, mongo, resource_fields
from datetime import datetime

class Books(Resource):
    @marshal_with(resource_fields, envelope='bool_list')
    def get(self):
        return [x for x in mongo.db.bookList.find()]

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type = str, required = True, help = 'No task title provided')
        parser.add_argument('price', type = str, required = True, help = 'No task price provided')
        args = parser.parse_args()

        if not args['title'] or not args['price']:
            abort(400)

        args = {}

        for k, v in parser.parse_args().iteritems():
            if k == 'price':
                    v = float(v)
            args[k] = v

        args['date_updated'] = datetime.utcnow()
        mongo.db.bookList.insert(args)
        return {'msg': 'create book ok'}, 200

api.add_resource(Books, '/books', endpoint = 'books')
# -*- encoding: utf-8 -*-
from flask_restful import Api, Resource

from .. import v1
from .models import User, UserSchema, db

schema = UserSchema()
api = Api(v1)


class UserList(Resource):
    def get(self):
        try:
            query_set = User.query.all()
            # Serializamos el query set indicando con many que es un array
            res = schema.dump(query_set, many=True).data
            return res, 200
        except Exception as e:
            # Excepción si falla la conexión
            return error_500()

api.add_resource(UserList, '/user')

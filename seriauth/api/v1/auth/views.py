# -*- encoding: utf-8 -*-
"""Modulo donde se crea el recurso de Tokens."""
from flask import request
from flask_restful import Api, Resource

from .. import blueprint_auth
from ...lib.errors import error_422
from .auth_user import auth_superuser, auth_user
from .models import TokenSchema

# http://flask.pocoo.org/
# https://flask-restful.readthedocs.io/en/0.3.5/

schema = TokenSchema()
api = Api(blueprint_auth)


class Tokens(Resource):
    """Recibe las peticiones [POST] del recurso tokens."""

    def post(self):
        """Crea un nuevo token de autentificación.

        :Parameters:

        - application/json
        """
        if request.content_type != "application/json":
            err = {"content_type": ["Se esperaba application/json"]}
            return error_422(err)
        else:
            json_data = request.get_json(force=True)
            if not json_data:
                err = {"datos": ["Información insuficientes."]}
                return error_422(err)
            data, errors = schema.load(json_data)
            req_type = data.get('type')
            req_exp = data.get('exp') if data.get('exp') is not None else 10080
            req_email = data.get('email')
            req_pw = data.get('password')

            if errors:
                return error_422(errors)
            elif req_type is None:
                return auth_user(req_email, req_pw, req_exp)
            elif req_type == "superuser":
                return auth_superuser(req_email, req_pw, req_exp)
            else:
                return auth_user(req_email, req_pw, req_exp)


api.add_resource(Tokens, '/tokens')

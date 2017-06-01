# -*- encoding: utf-8 -*-
"""Logica del manejo de los recursos."""
from flask import request
from flask_restful import Api, Resource

from .. import blueprint_users
from ...lib.encrypt import encrypt_sha512
from ...lib.errors import error_409, error_410, error_422, error_500
from ..emails.models import Email, EmailSchema
from .models import User, UserSchema

# http://flask.pocoo.org/
# https://flask-restful.readthedocs.io/en/0.3.5/

schema = EmailSchema()
schema_u = UserSchema()
api = Api(blueprint_users)


class UsersList(Resource):
    """Recibe las peticiones [GET,POST] del recurso users."""

    def get(self):
        """Obtiene un arreglo de Users."""
        try:
            query_set = User.query.all()
            res = schema_u.dump(query_set, many=True).data
            return res, 200
        except Exception as e:
            return error_500()

    def post(self):
        """Crea un nuevo User."""
        json_data = request.get_json()
        if not json_data:
            err = {"datos": ["Información insuficientes."]}
            return error_422(err)
        data_user, errors_u = schema_u.load(json_data)
        data_email, errors_e = schema.load(json_data)
        if errors_u or errors_e:
            if errors_e:
                errors = errors_e
            else:
                errors = errors_u
            return error_409(errors)
        try:
            password, sub = data_user['password'], data_email['email']
            email = Email.query.filter_by(email=sub).first()
            if email is None:
                user = User(password=encrypt_sha512(password, 10000, 10))
                user.add(user)
                email = Email(email=sub, user=user)
                email.add(email)
                res = schema_u.dump(user).data
                return res, 201
            else:
                err = {"sub": ["El usuario ya existe"]}
                return error_409(err)
        except Exception as e:
            return error_500()


class UserDetail(Resource):
    """Recibe las peticiones [GET,PUT,DELETE] del recurso users."""

    def get(self, id):
        """Obtener un Usuario."""
        try:
            query_set = User.query.get(id)
            if query_set is None:
                return error_410()
            else:
                res = schema_u.dump(query_set).data
                return res, 200
        except Exception as e:
            return error_500()

    def put(self, id):
        """Actualiza un Usuario."""
        json_data = request.get_json()
        if not json_data:
            err = {"datos": ["Información insuficientes."]}
            return error_422(err)
        data_user, errors_u = schema_u.load(json_data)
        if errors_u:
            errors = errors_u
            return error_409(errors)
        try:
            user = User.query.get(id)
            if user is None:
                return error_410()
            pw_sha = encrypt_sha512(data_user['password'], 10000, 10)
            setattr(user, 'password', pw_sha)
            user.update()
            res = schema_u.dump(user).data
            return res
        except Exception as e:
            return error_500()

    def delete(self, id):
        """Elimina un usuario."""
        try:
            user = User.query.get(id)
            if user is None:
                return error_410()
            else:
                user.delete(user)
                # res = make_response()
                # res.status_code = 204
                return None, 204
        except Exception as e:
            return error_500()


class UserEmailList(Resource):
    """Lista los emails de un usuario."""
    def get(self, user_id):
        """Obtener un Usuario."""
        try:
            query_set = User.query.get(user_id)
            if query_set is None:
                return error_410()
            else:
                res = schema_u.dump(query_set).data
                return res, 200
        except Exception as e:
            return error_500()

    def post(self, user_id):
        """Crea un nuevo email a un usuario en especifico."""
        json_data = request.get_json()
        if not json_data:
            err = {"datos": ["Información insuficientes."]}
            return error_422(err)
        data, errors = schema.load(json_data)
        if errors:
            return error_409(errors)
        try:
            user = User.query.filter_by(id=user_id).first()
            if user is None:
                return error_410()
            email = Email.query.filter_by(email=data['email']).first()
            if email is None:
                email = Email(email=data['email'], user=user)
                email.add(email)
                res = schema.dump(email).data
                return res, 201
            else:
                err = {"sub": ["El correo ya esta registrado"]}
                return error_409(err)
        except Exception as e:
            return error_500()


api.add_resource(UsersList, '/users')
api.add_resource(UserDetail, '/users/<int:id>')
api.add_resource(UserEmailList, '/users/<int:user_id>/emails')

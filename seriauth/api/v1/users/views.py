# -*- encoding: utf-8 -*-
from flask import jsonify, make_response, request
from flask_restful import Api, Resource

from .. import blueprint_users
from ...lib.encrypt import encrypt_sha512
from ...lib.errors import error_409, error_410, error_422, error_500
from ...lib.regex_validators import validate_password
from ..emails.models import Email, EmailSchema
from .models import User, UserSchema

schema = EmailSchema()
schema_u = UserSchema()
api = Api(blueprint_users)


# Recurso de Users
class UsersList(Resource):
    """Recibe las peticiones [GET,POST] del recurso users."""

    def get(self):
        """Obtiene un arreglo de Users."""
        try:
            query_set = User.query.all()
            # Serializamos el query set indicando con many que es un array
            res = schema_u.dump(query_set, many=True).data
            return res, 200
        except Exception as e:
            # Excepción si falla la conexión
            return error_500()

    def post(self):
        """Crea un nuevo User."""
        json_data = request.get_json()
        if not json_data:
            err = {"datos": ["Información insuficientes."]}
            return error_422(err)
        data_u, errors_u = schema_u.load(json_data)
        data, errors = schema.load(json_data)
        return jsonify({'algo': data, 'holi': data_u})
        if errors:
            return error_422(errors)
        # return data
        password, sub = data['user']['password'], data['email']
        email = Email.query.filter_by(email=sub).first()
        try:
            if email is None:
                user = User(password=password)
                user.add(user)
                email = Email(email=data['email'], user=user)
                email.add(email)
                query = Email.query.get(email.id)
                res = schema.dump(query).data
                return res, 201
            else:
                err = {"sub": ["El usuario ya existe"]}
                return error_409(err)

        except Exception as e:
            return error_500()


class UserDetail(Resource):
    """Recibe las peticiones [GET,PUT,DELETE] del recurso users."""

    def get(self, id):
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
        json_data = request.get_json(force=True)
        # Obtiene la información del request
        if not json_data:
            err = {"datos": ["Información insuficientes."]}
            return error_422(err)
        # validamos y deserializamos el request
        data, errors = schema.load(json_data)
        if errors:
            return error_422(errors)
        try:
            user = User.query.get(id)
            if user is None:
                return error_410()
            email, password = data['email'], data['password']
            pw_validate = validate_password(password)
            if not pw_validate:
                err = {"password": ["La contraseña no es válida."]}
                return error_422(err)
            password_sha = encrypt_sha512(password, 10000, 10)
            setattr(user, 'email', email)
            setattr(user, 'password', password_sha)
            user.update()
            return self.get(id)
        except Exception as e:
            return error_500()

    def delete(self, id):
        """Elimina al User con <id>.

        Parametros:
        id -- Entero
        """
        try:
            user = User.query.get(id)
            if user is None:
                return error_410()
            else:
                user.delete(user)
                res = make_response()
                res.status_code = 204
                return res
        except Exception as e:
            # Excepción si falla la conexión
            return error_500()


api.add_resource(UsersList, '/users')
api.add_resource(UserDetail, '/users/<int:id>')

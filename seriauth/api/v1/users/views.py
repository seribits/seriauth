# -*- encoding: utf-8 -*-
# from flask import Blueprint, request, make_response
from .models import Users, UsersSchema, db
from flask_restful import Api, Resource
from seriauth.lib.encrypt import encrypt_sha512
from seriauth.lib.regex_validators import validate_password
from seriauth.lib.errors import error_409, error_410, error_422, error_500

from seriauth.api.v1 import v1
# users = Blueprint('users', __name__)


schema = UsersSchema()
api = Api(v1)


# Recurso de Users
class UsersList(Resource):
    """Recibe las peticiones [GET,POST] del recurso users."""

    def get(self):
        """Obtiene un arreglo de Users."""
        try:
            query_set = Users.query.all()
            # Serializamos el query set indicando con many que es un array
            res = schema.dump(query_set, many=True).data
            return res, 200
        except Exception as e:
            # Excepción si falla la conexión
            return error_500()

    def post(self):
        """Crea un nuevo User."""
        # Valida que la petición sea <application/json>
        if request.content_type != "application/json":
            err = {"content_type": ["Se esperaba application/json"]}
            return error_422(err)
        else:
            # Obtiene la información del request
            json_data = request.get_json(force=True)
            if not json_data:
                err = {"datos": ["Información insuficientes."]}
                return error_422(err)
            # validamos y deserializamos el request
            data, errors = schema.load(json_data)

            if errors:
                return error_422(errors)
            try:
                email, password = data['email'], data['password']
                # Consulta si existe algún email igual
                query_set = Users.query.filter_by(email=email).first()
                # Validación con expresión regular
                pw_validate = validate_password(password)
                if not pw_validate:
                    err = {"password": ["La contraseña no es válida."]}
                    return error_422(err)

                if query_set is None:
                    # Crear el nuevo user
                    password_sha = encrypt_sha512(password, 10000, 10)
                    user = Users(
                        email=email,
                        password=password_sha
                    )
                    user.add(user)
                    query = Users.query.get(user.id)
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
        """Devuelve al User con <id>.

        Parametros:
        id -- Entero
        """
        try:
            # Consulta de User con <id>
            query_set = Users.query.get(id)
            if query_set is None:
                return error_410()
            else:
                # Serialización del query set
                res = schema.dump(query_set).data
                res.status_code = 200
                return res
        except Exception as e:
            # Excepción si falla la conexión
            return error_500()

    def put(self, id):
        """Actualiza al User con <id>.

        Parametros:
        id -- Entero
        """
        # Valida que la petición sea <application/json>
        if request.content_type != "application/json":
            err = {"content_type": ["Se esperaba application/json"]}
            return error_422(err)
        else:
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
                user = Users.query.get(id)
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
            user = Users.query.get(id)
            if user is None:
                return error_410()
            else:
                delete = user.delete(user)
                res = make_response()
                res.status_code = 204
                return res
        except Exception as e:
            # Excepción si falla la conexión
            return error_500()


api.add_resource(UsersList, '/users')
api.add_resource(UserDetail, '/users/<int:id>')

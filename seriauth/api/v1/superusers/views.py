# -*- encoding: utf-8 -*-
from flask import request, Blueprint, make_response
from .models import Superusers, SuperusersSchema, db
from flask_restful import Api, Resource
from seriauth.lib.encrypt import encrypt_sha512
from seriauth.lib.regex_validators import validate_password
from seriauth.lib.errors import error_409, error_410, error_422, error_500

from seriauth.api.v1 import v1

schema = SuperusersSchema()
api = Api(v1)


# Recurso de Superusers

class SuperusersList(Resource):
    """Recibe las peticiones [GET] del recurso superusers."""

    def get(self):
        """Obtiene un arreglo de Superusers."""
        try:
            # Consulta de todos los Superusers
            query_set = Superusers.query.all()
            # Serializamos el query set indicando con many que es un array
            res = schema.dump(query_set, many=True).data
            return res, 200
        except Exception as e:
            # Excepción si falla la conexión
            return error_500()


class SuperuserDetail(Resource):
    """Recibe las peticiones [GET,PUT,DELETE] del recurso superusers."""

    def get(self, id):
        """Devuelve al Superuser con <id>.

        Parametros:
        id -- Entero
        """
        try:
            # Consulta del Superuser con <id>
            query_set = Superusers.query.get(id)
            if query_set is None:
                return error_410()
            else:
                # Selización del query set
                res = schema.dump(query_set).data
                return res, 200

        except Exception as e:
            # Exception si falla la conexión
            return error_500()

    def put(self, id):
        """Actualiza al Superuser con <id>.

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
                superuser = Superusers.query.get(id)
                if superuser is None:
                    return error_410()
                username, email, password = (
                    data['username'], data['email'], data['password']
                )
                pw_validate = validate_password(password)
                if not pw_validate:
                    err = {"password": ["La contraseña no es válida."]}
                    return error_422(err)
                password_sha = encrypt_sha512(password, 10000, 10)
                setattr(superuser, 'username', username)
                setattr(superuser, 'email', email)
                setattr(superuser, 'password', password_sha)
                superuser.update()
                return self.get(id)
            except Exception as e:
                return error_500()

    def delete(self, id):
        """Elimina al Superuser con <id>.

        Parametros:
        id -- Entero
        """
        try:
            superuser = Superusers.query.get(id)
            if superuser is None:
                return error_410()
            else:
                delete = superuser.delete(superuser)
                res = make_response()
                res.status_code = 204
                return res
        except Exception as e:
            # Excepción si falla la conexión
            return error_500()


api.add_resource(SuperusersList, '/superusers')
api.add_resource(SuperuserDetail, '/superusers/<int:id>')

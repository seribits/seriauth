# -*- encoding: utf-8 -*-
"""Logica del recurso Emails."""
from flask import jsonify, make_response, request
from flask_restful import Api, Resource

from .. import blueprint_emails
from ...lib.errors import error_409, error_410, error_422, error_500
from .models import Email, EmailSchema

schema = EmailSchema()
api = Api(blueprint_emails)


class EmailList(Resource):

    def get(self):
        try:
            query_set = Email.query.all()
            res = schema.dump(query_set, many=True).data
            return res, 200
        except Exception as e:
            return error_500()


class EmailDetail(Resource):

    def get(self, id):
        try:
            query_set = Email.query.get(id)
            if query_set is None:
                return error_410()
            else:
                res = schema.dump(query_set).data
                return res, 200
        except Exception as e:
            return error_500()

    def put(self, id):
        """Actualiza un Ususrio."""
        json_data = request.get_json()
        if not json_data:
            err = {"datos": ["Información insuficientes."]}
            return error_422(err)
        data, errors = schema.load(json_data)
        if errors:
            return error_409(errors)
        try:
            email = Email.query.get(id)
            if email is None:
                return error_410()
            else:
                sub = data['email']
                setattr(email, 'email', sub)
                email.update()
                res = schema.dump(email).data
                return res, 200
                # return self.get(id)
        except Exception as e:
            return e

    def delete(self, id):
        """Elimina un usuario."""
        try:
            email = Email.query.get(id)
            if email is None:
                return error_410()
            else:
                email.delete(email)
                return None, 204
        except Exception as e:
            return error_500()


api.add_resource(EmailList, '/emails')
api.add_resource(EmailDetail, '/emails/<int:id>')

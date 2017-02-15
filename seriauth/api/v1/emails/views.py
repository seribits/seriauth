# -*- encoding: utf-8 -*-
from flask import jsonify, make_response, request
from flask_restful import Api, Resource

from .. import blueprint_emails
from ...lib.errors import error_410, error_500
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
                # res = schema.dump(query_set)
                # return jsonify({'res': "holi"})
        except Exception as e:
            return error_500()


api.add_resource(EmailList, '/emails')
api.add_resource(EmailDetail, '/emails/<int:id>')

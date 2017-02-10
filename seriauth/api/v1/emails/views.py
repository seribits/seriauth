# -*- encoding: utf-8 -*-

from flask_restful import Api, Resource

from .. import blueprint_emails
from ...lib.errors import error_500
from .models import Email, EmailSchema

schema = EmailSchema()
api = Api(blueprint_emails)


class EmailsList(Resource):
    def get(self):
        try:
            query_set = Email.query.all()
            res = schema.dump(query_set, many=True).data
            return res, 200
        except Exception as e:
            return error_500()


api.add_resource(EmailsList, '/emails')

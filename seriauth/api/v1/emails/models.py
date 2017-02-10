# -*_ encoding: utf-8 -*-
from marshmallow import Schema, ValidationError, fields, pre_load

from seriauth import db

from ..users.models import Users, UsersSchema


class Emails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('Users',
                            backref=db.backref('emails', lazy='dynamic'))


class EmailsSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Str()
    user = fields.Nested(UsersSchema)

    @pre_load
    def process_email(self, data):
        user = data.get('password')
        if user:
            user_dict = dict(password=user)
        else:
            user_dict = {}
        data['user'] = user_dict
        return data

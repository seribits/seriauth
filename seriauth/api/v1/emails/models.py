# -*_ encoding: utf-8 -*-
from marshmallow import Schema, fields, pre_load

from seriauth import db

from ..users.models import UserSchema


class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(
        'User', backref=db.backref('email', lazy='dynamic')
        )


class EmailSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Str()
    user = fields.Nested(UserSchema)

    @pre_load
    def process_email(self, data):
        user = data.get('password')
        if user:
            user_dict = dict(password=user)
        else:
            user_dict = {}
        data['user'] = user_dict
        return data

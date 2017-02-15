# -*_ encoding: utf-8 -*-
from marshmallow import Schema, fields, pre_load

from seriauth import db


class DAO():

    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()


class Email(db.Model, DAO):
    """Email."""

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class EmailSchema(Schema):
    """EmailSchema."""

    id = fields.Int(dump_only=True)
    email = fields.Email(
            required=True,
            load_from='sub',
            dump_to='sub',
            error_messages={
                'invalid': 'Email no válido.',
                'required': 'Atributo obligatorio.'
                }
        )
    user_id = fields.Int(dump_to='user')

"""    @pre_load
    def process_email(self, data):
        return {'sub': 'email2@seribits.com', 'user': 1}
        user = data.get('password')
        if user:
            user_dict = dict(password=user)
        else:
            user_dict = {}
        data['user'] = user_dict
        return data
"""
"""C.
class Email(db.Model, DAO):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(
        'User', backref=db.backref('email', lazy='dynamic')
        )

class EmailSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Email(
        required=True,
        load_from='sub',
        dump_to='sub',
        error_messages={
            'invalid': 'Email no válido.',
            'required': 'Atributo obligatorio.'
            }
        )
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
"""

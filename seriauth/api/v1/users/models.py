# -*- encoding: utf-8 -*-
from marshmallow import Schema, ValidationError, fields, pre_load, validates

from seriauth import db

from ..emails.models import EmailSchema


class DAO():
    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()

    def update(self):
        return db.session.commit()

    def delete(self, resource):
        db.session.delete(resource)
        return db.session.commit()


class User(db.Model, DAO):
    """User."""

    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.Text())
    email = db.relationship(
        'Email', backref=db.backref('user', lazy='joined'), lazy='dynamic'
        )


def must_not_be_blank(data):
    if not data:
        raise ValidationError('El atributo no puede ser nulo.')


class UserSchema(Schema):
    """PersonSchema."""

    id = fields.Int(dump_only=True)
    password = fields.Str(
        required=True,
        # load_only=True,
        validate=must_not_be_blank,
        error_messages={
            'invalid': 'No es un string válido.',
            'required': 'Atributo obligatorio.'
            }
        )
    email = fields.Nested(EmailSchema, only=['email'], many=True)

    @pre_load
    def process_email(self, data):
        email = data.get('sub')
        if email:
            email_dict =  email
        else:
            email_dict = ""
        data['email'] = email_dict
        return data


"""    @validates('password')
    def validate_password(self, data):
        if len(data) < 8:
            raise ValidationError('Password must be more than 8 characters')
"""
#    class Meta:
#        # type_ = 'user'
#        fields = ("id", "password", "email")


"""C.
class User(db.Model, DAO):
    id = db.Column(db.Integer, primary_key=True)
    creation_time = db.Column(
        db.TIMESTAMP,
         server_default=db.func.current_timestamp(),
        nullable='False'
        )
    creation_time = db.Column(db.DateTime)
    is_active = db.Column(
        db.Boolean,
        server_default='True',
        nullable=False
        )
    password = db.Column(db.Text(), nullable=False)


class UserSchema(Schema):
    id = fields.Integer(dump_only=True)  # solo lectura dump_only=True
    password = fields.String(
        required=True,
        load_only=True,
        validate=must_not_be_blank,
        error_messages={
            'invalid': 'No es un string válido.',
            'required': 'Atributo obligatorio.'
            }
        )
    # is_active = fields.Boolean(dump_only=True)

    class Meta:
        # type_ = 'user'
        fields = ("id", "password")
        """

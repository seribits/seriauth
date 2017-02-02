# -*- encoding: utf-8 -*-
from collections import OrderedDict

from marshmallow import Schema, ValidationError, fields

from seriauth import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.relationship('Email', backref='user', lazy='dynamic')
    password = db.Column(db.Text(), nullable=False)

class Username(User):
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    username = db.Column(db.String, nullable=False)


class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    password = fields.String()

    class Meta:
        type_ = 'user'
        fields = ("id", "password")

class EmailSchema(Schema):
    id = fields.Integer(dump_only=True)
    email = fields.Email(
        required=True,
        load_from='sub',
        dump_to='sub',
        error_messages={
            'invalid': 'Email no válido.',
            'required': 'Atributo obligatorio.'
        }
    )

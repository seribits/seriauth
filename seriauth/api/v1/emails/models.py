# -*_ encoding: utf-8 -*-
from marshmallow import Schema, ValidationError, fields

from seriauth import db


class Emails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    person_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class EmailsSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Str()

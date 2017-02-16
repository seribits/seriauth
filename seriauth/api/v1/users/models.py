# -*- encoding: utf-8 -*-
"""Modelo y Esquema de User."""
import re

from marshmallow import Schema, ValidationError, fields, validates

from seriauth import db

from ..emails.models import EmailSchema


class User(db.Model):
    """Modelo User."""

    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.Text())
    email = db.relationship(
        'Email', backref=db.backref(
            'user', lazy='joined'), lazy='dynamic', cascade='delete'
    )

    def add(self, resource):
        """Nuevo."""
        db.session.add(resource)
        return db.session.commit()

    def update(self):
        """Actualizar."""
        return db.session.commit()

    def delete(self, resource):
        """Eliminar."""
        db.session.delete(resource)
        return db.session.commit()


def must_not_be_blank(data):
    """Validación de campos nulos."""
    if not data:
        raise ValidationError('El atributo no puede ser nulo.')


class UserSchema(Schema):
    """PersonSchema."""

    id = fields.Int(dump_only=True)
    password = fields.Str(
        required=True,
        load_only=True,
        validate=must_not_be_blank,
        error_messages={
            'invalid': 'No es un string válido.',
            'required': 'Atributo obligatorio.'
        }
    )
    email = fields.Nested(EmailSchema, only=['email'], many=True)

    @validates('password')
    def validate_password(self, data):
        """Validación del atributo [password]."""
        pattern_password = (
            '(?=.*[A-Z])(?=.*[!#$%&/()?¿¡@;*])(?=.*[0-9])(?=.*[a-z]).{8,15}'
        )
        if re.match(pattern_password, data):
            pass
        else:
            raise ValidationError('La contraseña no es valida')

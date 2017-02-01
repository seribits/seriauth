# -*- encoding: utf-8 -*-
from collections import OrderedDict

from marshmallow import Schema, ValidationError, fields

from seriauth import db


class DAO():
    """Ejecuta los cambios del recurso Superusers."""

    def update(self):
        """Realiza la actualización del recurso Superusers."""
        return db.session.commit()

    def delete(self, resource):
        """Realiza la eliminación del recurso Superusers.

        Argumentos:
        resource - Objeto del tipo Superusers
        """
        db.session.delete(resource)
        return db.session.commit()


class Superusers(db.Model, DAO):
    """Estructura básica del recurso Users."""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    creation_time = db.Column(
        db.TIMESTAMP,
        server_default=db.func.current_timestamp(),
        nullable='False'
    )
    is_active = db.Column(db.Boolean, server_default='True', nullable=False)
    password = db.Column(db.Text(), nullable=False)
    permissions = db.Column(db.ARRAY(db.String, dimensions=1), nullable=False)

    def __init__(self,  username, email, password, permissions):
        """Constructor de Superusers.

        Argumentos:
        username - nombre del superusuario
        email - correo
        password - contraseña
        permissions - Array de permisos
        """
        self.username = username
        self.email = email
        self.password = password
        self.permissions = permissions


# validator de campos vacíos

def must_not_be_blank(data):
    """Validación de atributos vacios.

    Argumentos:
    data - valor del atributo
    """
    if not data:
        raise ValidationError('El atributo no puede ser nulo.')


# Schema Superusers

class SuperusersSchema(Schema):
    """Estructura de Superusers del tipo Schema."""

    # atributo id autoincrementable y de solo lectura dump_only=True
    id = fields.Integer(dump_only=True)
    username = fields.String(
        required=True,
        load_from='sub',
        dump_to='sub',
        validate=must_not_be_blank,
        error_messages={
            'invalid': 'No es un string válido.',
            'required': 'Atributo obligatorio.'
        }
    )
    email = fields.Email(
        required=True,
        error_messages={
            'invalid': 'Email no válido.',
            'required': 'Atributo obligatorio.'
        }
    )
    password = fields.String(
        required=True,
        load_only=True,
        validate=must_not_be_blank,
        error_messages={
            'invalid': 'No es un string válido.',
            'required': 'Atributo obligatorio.'
        }
    )
    is_active = fields.Boolean(dump_only=True)

    class Meta:
        type_ = 'superusers'
        fields = ("id", "username", "email", "is_active", "password")
        ordered = True

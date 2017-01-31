# -*- encoding: utf-8 -*-
from marshmallow import Schema, fields, ValidationError
from sqlalchemy.exc import SQLAlchemyError
from collections import OrderedDict
from seriauth import db


class DAO():
    """Ejecuta los cambios del recurso Users."""

    def add(self, resource):
        """Realiza la creación del recurso Users.

        Argumentos:
        resource - Objeto del tipo Users
        """
        db.session.add(resource)
        return db.session.commit()

    def update(self):
        """Realiza la actualización del recurso Users."""
        return db.session.commit()

    def delete(self, resource):
        """Realiza la eliminación del recurso Users.

        Argumentos:
        resource - Objeto del tipo Users
        """
        db.session.delete(resource)
        return db.session.commit()


class Users(db.Model, DAO):
    """Estructura básica del recurso Users."""

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    creation_time = db.Column(
        db.TIMESTAMP,
        server_default=db.func.current_timestamp(),
        nullable='False'
    )
    is_active = db.Column(
        db.Boolean,
        server_default='True',
        nullable=False
    )
    password = db.Column(db.Text(), nullable=False)

    def __init__(self,  email, password):
        """Constructor de Users.

        Argumentos:
        email - correo
        password - contraseña
        """
        self.email = email
        self.password = password


def must_not_be_blank(data):
    """Validación de atributos vacios.

    Argumentos:
    data - valor del atributo
    """
    if not data:
        raise ValidationError('El atributo no puede ser nulo.')


class UsersSchema(Schema):
    """Estructura de Users del tipo Schema."""

    id = fields.Integer(dump_only=True)  # solo lectura dump_only=True
    email = fields.Email(
        required=True,
        load_from='sub',
        dump_to='sub',
        validate=must_not_be_blank,
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
        type_ = 'users'
        fields = ("id", "email", "is_active", "password")
        ordered = True

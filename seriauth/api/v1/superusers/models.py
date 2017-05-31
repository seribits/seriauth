# -*- encoding: utf-8 -*-
from marshmallow import Schema, ValidationError, fields

from seriauth import db


class Superuser(db.Model):
    """Estructura básica del recurso Superusers."""

    # Especificando el nombre del identificador cuando se usan multiples bd.
    __bind_key__ = 'superusers'

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

        :Parameters:

        - username [str] - nombre del superusuario.
        - email [str] - correo del superusuario.
        - password [str] - contraseña del superusuario.
        - permissions [array]- permisos del superusuario.
        """
        self.username = username
        self.email = email
        self.password = password
        self.permissions = permissions

    def update(self):
        """Realiza la actualización del recurso Superusers."""
        return db.session.commit()

    def delete(self, resource):
        """Realiza la eliminación del recurso Superusers.

        :Parameters:

        - resource [Superusers] - Objeto del tipo Superusers
        """
        db.session.delete(resource)
        return db.session.commit()


# validator de campos vacíos
def must_not_be_blank(data):
    """Validación de atributos vacios.

    :Parameters:

    - data - valor del atributo
    """
    if not data:
        raise ValidationError('El atributo no puede ser nulo.')


# Schema Superusers

class SuperuserSchema(Schema):
    """Estructura de Superusers del tipo Schema.

        :note: Se encarga de la serialización y deserialización del objeto.
    """

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

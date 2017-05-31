# -*- encoding: utf-8 -*-
"""Modulo con la estructura para la autenticación."""
from marshmallow import Schema, ValidationError, fields


# validator de campos vacíos
def must_not_be_blank(data):
    """Validación de atributos vacios.

    :Parameters:

    - data - valor del atributo.
    """
    if not data:
        raise ValidationError('El atributo no puede ser nulo.')


# Schema Tokens

class TokenSchema(Schema):
    """Estructura del Token del tipo Schema."""

    # atributo id autoincrementable y de solo lectura dump_only=True
    email = fields.String(
        required=True,
        load_from='sub',
        validate=must_not_be_blank,
        error_messages={
            'invalid': 'atributo no válido.',
            'required': 'Atributo obligatorio.'
        }
    )
    exp = fields.Integer(
        required=False,
        load_only=True,
        validate=must_not_be_blank,
        error_messages={
            'invalid': 'Atributo no válido debe ser de tipo entero.'
        }
    )
    type = fields.String(
        required=False,
        load_only=True,
        validate=must_not_be_blank,
        error_messages={
            'invalid': 'Atributo no válido.'
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

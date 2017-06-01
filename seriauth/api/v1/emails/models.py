# -*_ encoding: utf-8 -*-
"""Modelo y Esquema del modelo Email."""
from marshmallow import Schema, fields

from seriauth import db


# http://marshmallow.readthedocs.io/en/latest/quickstart.html


class Email(db.Model):
    """Clase del modelo Email."""

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def add(self, resource):
        """Agrega un Email."""
        db.session.add(resource)
        return db.session.commit()

    def update(self):
        """Actualiza un Email."""
        return db.session.commit()

    def delete(self, resource):
        """Eliminar un Email."""
        db.session.delete(resource)
        return db.session.commit()


class EmailSchema(Schema):
    """Clase con la estructura de validación para el modelo Email."""

    id = fields.Int(dump_only=True)
    email = fields.Email(
        required=True,
        load_from='sub',
        # dump_to='sub',
        error_messages={
            'invalid': 'Email no válido.',
            'required': 'Atributo obligatorio.'
        }
    )
    user_id = fields.Int(dump_to='user')

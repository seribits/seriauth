# -*_ encoding: utf-8 -*-
"""Modelo y Esquema de Email."""
from marshmallow import Schema, fields

from seriauth import db


class Email(db.Model):
    """Email."""

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def add(self, resource):
        """Metodo para agregar."""
        db.session.add(resource)
        return db.session.commit()

    def update(self):
        """Actualiza."""
        return db.session.commit()

    def delete(self, resource):
        """Eliminar."""
        db.session.delete(resource)
        return db.session.commit()


class EmailSchema(Schema):
    """EmailSchema."""

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

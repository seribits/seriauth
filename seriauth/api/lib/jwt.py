# -*- encoding: utf-8 -*-
"""Modulo encargado de crear y mostrar un Token."""
import os

from jose import jwt

# http://python-jose.readthedocs.io/en/latest/jwt/api.html

jwt_secret = os.environ['SERIAUTH_JWT_SECRET']


def encode_token(claims):
    """Crea un token de autentificación.

    :Parameters:
    - claims [dict] - Objeto a cifrar

    :rtype: str
    """
    token = jwt.encode(claims, jwt_secret, algorithm='HS256')
    return token


def decode_token(token):
    """Descifra un token.

    :Parameters:
    - token  [str] - token que deseamos transformar.

    :rtype: str
    """
    payload = jwt.decode(token, jwt_secret, algorithms=['HS256'])
    return payload

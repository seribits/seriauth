# -*- encoding: utf-8 -*-
import os

from jose import jwt

jwt_secret = os.environ['SERIAUTH_JWT_SECRET']


def encode_token(claims):
    """Crea un token de autentificación.

    Argumentos:
    claims - Objeto por cifrar
    """
    token = jwt.encode(claims, jwt_secret, algorithm='HS256')
    return token


def decode_token(token):
    """Descifra un token.

    Argumentos:
    token - Objeto por descifrar
    """
    payload = jwt.decode(token, jwt_secret, algorithms=['HS256'])
    return payload

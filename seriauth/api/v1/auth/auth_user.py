# -*- encoding: utf-8 -*-
from datetime import datetime, timedelta

from flask import jsonify

from ...lib import jwt
from ...lib.encrypt import check_sha512
from ...lib.errors import error_409, error_410, error_500
from ..emails.models import Email, EmailSchema
from ..superusers.models import Superuser
from ..users.models import User

schema = EmailSchema()

def auth_superuser(req_username, req_password, req_exp):
    """Valida información y otorga token a Superuser.

    Argumentos:
    req_username - Usuario
    req_password - Contraseña
    req_exp - Tiempo de expiración del token
    """
    try:
        expiration = req_exp if req_exp is not None else 10080
        expiration = expiration if expiration < 11000 else 10080
        user = Superuser.query.filter_by(username=req_username).first()
        if user is None:
            res = error_410()
        else:
            username = user.username
            hash_encrypt = user.password
            validate = check_sha512(req_password, hash_encrypt)
            if validate and (username == req_username):
                expire = (
                    datetime.utcnow() + timedelta(minutes=expiration)
                )
                token = {
                    "type": "superuser",
                    "sub": user.username,
                    "exp": expire,
                    "id": user.id,
                    "email": user.email,
                    "is_active": user.is_active,
                    "permissions": {
                        "everything": user.permissions
                    }
                }
                results = jwt.encode_token(token)
                res = jsonify({"token": results})
                res.status_code = 201
            else:
                err = ({
                    "sub": ["Dato incorrecto"],
                    "password": ["Dato incorrecto."]
                })
                res = error_409(err)
            return res
        return res

    except Exception as e:
        return error_500()


def auth_user(req_email, req_password, req_exp):
    """Valida información y otorga token a User.

    Argumentos:
    req_email - Correo
    req_password - Contraseña
    req_exp - Tiempo de expiración del token
    """
    try:
        expiration = req_exp if req_exp is not None else 10080
        expiration = expiration if expiration < 11000 else 10080
        object_email = Email.query.filter_by(email=req_email).first()
        # data_email = schema.dump(search_email).data
        object_user = User.query.filter_by(id=object_email.user_id).first()
        if object_user is None:
            res = error_410()
        else:
            email = object_email.email
            hash_encrypt = object_user.password
            validate = check_sha512(req_password, hash_encrypt)
            if validate and (req_email == email):
                expire = (
                    datetime.utcnow() + timedelta(minutes=expiration)
                )
                token = {
                    "type": "user",
                    "sub": email,
                    'exp': expire,
                    "id": object_user.id,
                    "email": email,
                    "permissions:": {}
                }
                results = jwt.encode_token(token)
                res = jsonify({"token": results})
                res.status_code = 201
            else:
                err = ({
                    "sub": ["Dato incorrecto"],
                    "password": ["Dato incorrecto."]
                })
                res = error_409(err)
            return res
        return res

    except Exception as e:
        return error_500()

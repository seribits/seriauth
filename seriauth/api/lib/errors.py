# -*- encoding: utf-8 -*-
"""Modulo para creación de errores."""
from flask import jsonify


# http://flask.pocoo.org

def error_409(error):
    """Genera un objeto JSON para el error 409.

    :Parameters:
    - error [str] - Mensaje que especifica cual fue el error.

    :rtype: response
    """
    response = jsonify({"error": error})
    response.status_code = 409
    return response


def error_410():
    """Genera un objeto JSON para el error 410.

    :rtype: response
    """
    response = jsonify(
        {"error": {"recurso": ["El recurso solicitado no existe."]}}
    )
    response.status_code = 410
    return response


def error_422(error):
    """Genera un objeto JSON para el error 422.

    :Parameters:

    - error - String especifica cual fue el error.

    :rtype: response

    """
    response = jsonify({"error": error})
    response.status_code = 422
    return response


def error_500():
    """Genera un objeto JSON para el error 500.

    :rtype: response
    """
    response = jsonify(
        {"error": {"BD": ["Sin conexión."]}}
    )
    response.status_code = 500
    return response

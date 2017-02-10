# -*- encoding: utf-8 -*-
from flask import jsonify


def error_409(error):
    """Genera un objeto JSON para el error 409.

    Argumentos:
    error - String especifica cual fue el error.
    """
    response = jsonify({"error": error})
    response.status_code = 409
    return response


def error_410():
    """Genera un objeto JSON para el error 410."""
    response = jsonify(
        {"error": {"recurso": ["El recurso solicitado no existe."]}}
        )
    response.status_code = 410
    return response


def error_422(error):
    """Genera un objeto JSON para el error 422.

    Argumentos:
    error - String especifica cual fue el error.
    """
    response = jsonify({"error": error})
    response.status_code = 422
    return response


def error_500():
    """Genera un objeto JSON para el error 500."""
    response = jsonify(
        {"error": {"BD": ["Sin conexión."]}}
        )
    response.status_code = 500
    return response

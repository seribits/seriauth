# -*- encoding: utf-8 -*-
"""Modulo de validación de emails."""
import re


def validate_email(email):
    """Valida un email.

    :Parameters:

    - email [str] - Email de un usuario.

    :rtype: bool
    """
    pattern = '[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,6}'
    if re.match(pattern, email.lower()):
        return True
    else:
        return False
    """
    [\w.%+-] - usuario: Cualquier caracter alfanumerico mas los signos (.%+-)
    +@              seguido de @
    [\w.-] - dominio: Cualquier caracter alfanumerico mas los signos (.-)
    +\. - seguido de .
    [a-zA-Z]{2,6} - dominio: 2 a 6 letras en minúsculas o mayúsculas.
    """


def validate_password(password):
    """Valida una contraseña.

    :Parameters:

    - password [str] - Contraseña de un usuario.

    :rtype: bool
    """
    pattern_password = (
        '(?=.*[A-Z])(?=.*[!#$%&/()?¿¡@;*])(?=.*[0-9])(?=.*[a-z]).{8,15}'
    )
    if re.match(pattern_password, password):
        return True
    else:
        return False

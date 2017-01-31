# -*- encoding: utf-8 -*-
import re


def validate_email(email):
    """Valida un email.

    Argumentos:
    email - String a validar
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

    Argumentos:
    password - String a validar
    """
    pattern_password = '(?=.*[A-Z])(?=.*[!#$%&/()?¿¡@;*])(?=.*[0-9])(?=.*[a-z]).{8,15}'
    if re.match(pattern_password, password):
        return True
    else:
        return False

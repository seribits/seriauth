# -*- encoding: utf-8 -*-
from passlib.hash import pbkdf2_sha512


def encrypt_sha512(password, rounds, salt):
    """Devuelve un string cifrado.

    :Parameters:

    - password [str] - Cadena a cifrar
    - rounds [int] - Iteraciones a utilizar, default(12000) max(999999999).
    - salt [int] - Salto criptográfica valor en bytes entre 0 y 1024.

    :rtype: str
    """
    rounds = rounds if rounds is not None else 12000
    salt = salt if salt is not None else 12
    if password is None:
        password_encrypt = "Password field empty"
    else:
        password_encrypt = pbkdf2_sha512.encrypt(
            password, rounds=rounds, salt_size=salt
        )
    return password_encrypt


def check_sha512(unknown_password, valid_password):
    """Valida un String y un String cifrado.

    :Parameters:

    - unknown_password [str] - Cadena a comparar
    - valid_password [str] - Cadena cifrado
    """
    if unknown_password is None or valid_password is None:
        return "Sin parametros"
    else:
        return pbkdf2_sha512.verify(unknown_password, valid_password)

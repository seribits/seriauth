#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""Modulo con la utilería para la creación de un Superusuario."""
import getpass
import os

# http://docs.sqlalchemy.org/en/latest/orm/
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config.production import SQLALCHEMY_BINDS
from seriauth.api.lib.encrypt import encrypt_sha512
from seriauth.api.lib.regex_validators import validate_email, validate_password
from seriauth.api.v1.superusers.models import Superuser

# Asigna los Permisos de la variable de entorno de configuración.
super_permissions = os.environ['SERIAUTH_SUPER_PERMISSIONS_SECRET']

# Especificación de la conexión
engine = create_engine(SQLALCHEMY_BINDS['superusers'])

Session = sessionmaker(bind=engine)
session = Session()


def create_superuser():
    """Crea un Superusuario.

    :Parameters:

    - username (str) - Nombre del usuario.
    - email (str) - Email del usuario.
    - password (str) - Contraseña del usuario.

    :note:

    Los parametros que recibe se dan por línea de comando.
    """
    print("Nuevo administrador")
    username = input("Ingrese su Usuario: ")
    email = input("Ingrese su Correo: ")
    while not validate_email(email):
        print("¡Correo incorrecto, veriquelo por favor!")
        email = input("email: ")
    password = getpass.getpass("Ingrese su Contraseña: ")
    while not validate_password(password):
        print("¡Contraseña incorrecto, veriquelo por favor!")
        print("Debe tener 1 letra minúscula y 1 mayúscula")
        print("1 numero y 1 caracter especial [!#$%&/()?¿¡@;*] ")
        print("Debe ser contener de 8 a 15 caracteres")
        password = getpass.getpass("Ingrese su Contraseña: ")
    password = encrypt_sha512(password, 10000, 10)
    try:
        q_username = (
            session.query(Superuser).filter_by(username=username).count()
        )
        q_email = session.query(Superuser).filter_by(email=email).count()
        if q_username > 0 or q_email > 0:
            print("¡Usuario o Correo, ya existen :( ! Intentelo nuevamente")
        else:
            permissions = super_permissions.split()
            superuser = Superuser(
                username=username, email=email,
                password=password, permissions=permissions
            )
            try:
                session.add(superuser)
                session.commit()
                print("¡Administrador creado Correctamente :)!")
                print('Usuario: {}'.format(username))
                print('Correo: {}'.format(email))
            except Exception as e:
                print('¡ Error interno de validación :) ! ')
    except Exception as e:
        print('¡ No tenemos conexión a la BD :( !')


if __name__ == '__main__':
    create_superuser()

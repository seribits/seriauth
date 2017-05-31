# -*- encoding: utf-8 -*-
"""Modulo que contiene variables de entorno 'development'."""
import os

# Variables Flask
HOST = '0.0.0.0'
DEBUB = 'True'
BCRYPT_LEVEL = 12
PORT = 5000
SECRET_KEY = os.environ['SERIAUTH_FLASK_SECRET']

# Logging
LOG_PATH = 'logs/error.log'
LOG_LEVEL = 'DEBUG'

# Variables SQLALCHEMY
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = True

# Variable de conexión de SQLALCHEMY
SQLALCHEMY_DATABASE_URI = (
    # Configuración de la base de datos
    "{DB_SGDB}://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(
        DB_SGDB=os.environ['SERIAUTH_DB_SGDB'],
        DB_USER=os.environ['SERIAUTH_DB_USERNAME_SECRET'],
        DB_PASS=os.environ['SERIAUTH_DB_PASSWORD_SECRET'],
        DB_ADDR=os.environ['SERIAUTH_DB_HOST_SECRET'],
        DB_NAME=os.environ['SERIAUTH_DB_NAME_SECRET']
    )
)

# Configurar en caso de usar multiples bases de datos en el proyecto.
SQLALCHEMY_BINDS = {}

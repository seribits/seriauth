# -*- encoding: utf-8 -*-
# Variables Flask
HOST = '0.0.0.0'
DEBUB = True
BCRYPT_LEVEL = 12
PORT = 5000
SECRET_KEY  =  'Secret Key Default'

# Logging
LOG_PATH = 'logs/error.log'
LOG_LEVEL = 'DEBUG'

# Variables SQLALCHEMY
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = True

# Variable de conexión de SQLALCHEMY
SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/default.db'

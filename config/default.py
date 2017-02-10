# -*- encoding: utf-8 -*-
import os

# Variables Flask
HOST = '0.0.0.0'
DEBUG = 'True'
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
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'seriauth.db')
SQLALCHEMY_BINDS = {
    'superusers':'sqlite:///' + os.path.join(basedir, 'superusers.db')
}

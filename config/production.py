# -*- encoding: utf-8 -*-
# Variables Flask
HOST = "0.0.0.0"
DEBUB = False
BCRYPT_LEVEL = 12
PORT = 5000
SECRET_KEY = os.environ['FLASK_SECRET']

# Logging
LOG_PATH=logs/error.log
LOG_LEVEL=debug

# Variables SQLALCHEMY
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Variable de conexión de SQLALCHEMY
SQLALCHEMY_DATABASE_URI = (
    # Configuración de la base de datos
    "{DB_SGDB}://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(
        DB_SGDB=os.environ['DB_SGDB'],
        DB_USER=os.environ['DB_USERNAME_SECRET',
        DB_PASS=os.environ['DB_PASSWORD_SECRET'],
        DB_ADDR=os.environ['DB_HOST_SECRET'],
        DB_NAME=os.environ['DB_NAME_SECRET']
    )
)

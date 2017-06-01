# -*- encoding: utf-8 -*-
"""Asigna los valores de configuración a la aplicación de Flask."""
import os


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from logging.handlers import RotatingFileHandler

# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/
# http://flask.pocoo.org/
# https://docs.python.org/3.5/library/logging.handlers.html
db = SQLAlchemy()


def create_app(config_filename):
    """Creación de la instancia de Flask.

    :Parameters:

    - config_filename - (config.*) - Archivo con la configuración.

    :rtype: Objeto Flask
    """
    app = Flask(__name__)

    # Allow cross-domain access to API.
    # cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Load the default configuration
    app.config.from_object(config_filename)

    # Load the configuration from the instance folder
    # app.config.from_pyfile('config.py')

    # Load the file specified by the APP_CONFIG_FILE environment variable
    # Variables defined here will override those in the default configuration
    # *app.config.from_envvar('APP_CONFIG_FILE')

    # Configure logging.
    configure_logging(app)

    # Configure Database
    db.init_app(app)

    # Init modules
    init_modules(app)

    return app


def configure_logging(app):
    """Configuración del registro de la Aplicación.

    :Parameters:

    - app - Objeto Flask
    """
    log_path = app.config['LOG_PATH']
    log_level = app.config['LOG_LEVEL']

    # Si la ruta del directorio no existe la crea.
    log_dir = os.path.dirname(log_path)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    # Crea y registra el manejador de errores.
    log_handler = RotatingFileHandler(log_path, maxBytes=250000, backupCount=5)
    log_handler.setLevel(log_level)
    app.logger.addHandler(log_handler)

    # El primer registro informa a dónde estamos registrando.
    # Un tonto, pero sirve como una confirmación de que funciona.
    app.logger.info('Logging to: {}'.format(log_path))


def init_modules(app):
    """Importa los blueprints de los modulos de la API."""
    from .api.v1 import (
        blueprint_users, blueprint_auth, blueprint_superusers, blueprint_emails
    )
    from .home.views import home

    app.register_blueprint(home, url_prefix='/')
    app.register_blueprint(blueprint_users, url_prefix='/api/v1')
    app.register_blueprint(blueprint_auth, url_prefix='/api/v1')
    app.register_blueprint(blueprint_superusers, url_prefix='/api/v1')
    app.register_blueprint(blueprint_emails, url_prefix='/api/v1')

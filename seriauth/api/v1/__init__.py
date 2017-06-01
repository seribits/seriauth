# -*- encoding: utf-8 -*-
"""Modulo de creación de blueprints y obtener los recursos."""
from flask import Blueprint

# http://flask.pocoo.org/docs/0.12/blueprints/

blueprint_users = Blueprint('blueprint_users', __name__)
blueprint_auth = Blueprint('blueprint_auth', __name__)
blueprint_superusers = Blueprint('blueprint_superusers', __name__)
blueprint_emails = Blueprint('blueprint_emails', __name__)

from .superusers import views
from .auth import views
from .users import views
from .emails import views

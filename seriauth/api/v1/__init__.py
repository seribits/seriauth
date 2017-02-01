# -*- encoding: utf-8 -*-
from flask import Blueprint

v1 = Blueprint('v1', __name__)

from seriauth.api.v1.users import views
from seriauth.api.v1.superusers import views
from seriauth.api.v1.auth import views

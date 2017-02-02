# -*- encoding: utf-8 -*-
from flask import Blueprint

v1 = Blueprint('v1', __name__)

from .auth import views
from .users import views
from .superusers import views

#Test types of authentication
from .login import views

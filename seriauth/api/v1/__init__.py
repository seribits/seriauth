# -*- encoding: utf-8 -*-
from flask import Blueprint

# v1 = Blueprint('v1', __name__)
blueprint_users = Blueprint('blueprint_users', __name__)
blueprint_auth = Blueprint('blueprint_auth', __name__)
blueprint_superusers = Blueprint('blueprint_superusers', __name__)
blueprint_emails = Blueprint('blueprint_emails', __name__)

from .auth import views
from .users import views
from .superusers import views
from .emails import views
#Test types of authentication
# from .login import views

# -*- encoding: utf-8 -*-
"""Views home."""
from flask import Blueprint

home = Blueprint('home', __name__)


@home.route('', methods=['GET'])
def index():
    """Render the App index page."""
    return "Welcome"

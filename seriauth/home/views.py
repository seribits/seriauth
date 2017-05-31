# -*- encoding: utf-8 -*-
"""Vista de inicio."""
from flask import Blueprint

home = Blueprint('home', __name__)


@home.route('', methods=['GET'])
def index():
    """Muestra una vista de inicio."""
    return "Welcome"

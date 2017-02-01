# -*- encoding: utf-8 -*-
from flask import Blueprint

home = Blueprint('home', __name__)


@home.route('', methods=['GET'])
def index():
    ''' Renders the App index page.
    :return:
    '''
    return "Welcome"

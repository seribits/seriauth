# -*- encoding: utf-8 -*-
from flask import Blueprint, jsonify

home = Blueprint('home', __name__)


@home.route('/', methods=['GET'])
def index():
    ''' Renders the App index page.
    :return:
    '''
    return jsonify({
        "urls": [
            "/api/v1",
            "/api/v1/hello"
        ]
    })

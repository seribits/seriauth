#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import argparse
import os
from seriauth import create_app

# Create the flask app.
app = create_app('config.development')

# Run the app
if __name__ == '__main__':
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG']
    )

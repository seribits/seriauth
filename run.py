#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""Utilidad principal para iniciar la aplicación."""
# Importamos la función create_app que retorna una instancia de Flask
from seriauth import create_app

# Crea una instancia de flask.
app = create_app('config.production')

# Ejecuta la aplicación
if __name__ == '__main__':
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG']
    )

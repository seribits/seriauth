#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""Modulo con la utilería de línea de comando."""
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from run import app
from seriauth import db

"""Modulo de migración de las tablas a la base de datos."""

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

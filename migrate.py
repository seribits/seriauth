
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""Modulo de migración de las tablas a la base de datos."""
from auth import db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from run import app

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

# -*- encoding: utf-8 -*-
from seriauth import db

class Base(db.Model):
    id = db.Column(db.TEXT, primary_key=True)
    name = db.Column(db.TEXT)

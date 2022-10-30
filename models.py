from flask_login import UserMixin
from __init__ import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    dep_id =  db.Column(db.Integer)
    rol_id =  db.Column(db.Integer)
from app import db
from flask_login import UserMixin





class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.Boolean, default=False)
    username = db.Column(db.String(30), unique=True)
    email = db.Column(db.String(50), unique=True)
    firstname = db.Column(db.String(50), unique=False)
    lastname = db.Column(db.String(50), unique=False)
    password = db.Column(db.String(80))

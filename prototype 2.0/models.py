from app import db
from datetime import datetime


class User(db.Model):
    # See http://flask-sqlalchemy.pocoo.org/2.0/models/#simple-example
    # for details on the column types.

    # We always need an id
    id = db.Column(db.Integer, primary_key=True)

    # A dessert has a name, a price and some calories:
    name = db.Column(db.String(100))
    username = db.Column(db.Float)
    last_login = db.Column(db.Integer)
    email = db.Column(db.String(120), unique = False, nullable = True)

    def __init__(self, name, username, email):
        self.name = name
        self.username = username
        self.last_login = datetime.now()
        self.email = email

    def get_username(self):
        return self.calories / self.price


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     username = db.Column(db.String(80), unique=True)
#     email = db.Column(db.String(120), unique=False, nullable=True)
#
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email
#
#     def __repr__(self):
#         return '<User[%s] %s, %s>' % (self.id, self.username, self.email)
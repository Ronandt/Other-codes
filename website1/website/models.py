from math import e
from re import L
from . import db #from website, import db which is SQLAlchemy() instance
from flask_login import UserMixin #helps logins in
from sqlalchemy.sql import func
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True) #incremented
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone = True), default=func.now()) #store default vlaue for date
    #foreign key references column of another database to another column
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #Type of column is integer and by specificng foreweing, key you must pass a valid id of an existing user (one to many relaionsih[])
class User(db.Model, UserMixin): #user object needs to inherit from usermixin etc 
    id = db.Column(db.Integer, primary_key=True) #primary key unique object
    email = db.Column(db.String(150), unique=True) #no use can have the same email as another user
    password = db.Column(db.String(150))
    notes = db.relationship('Note')
#telling your object has to confirm to these rules

#https://docs.sqlalchemy.org/en/14/core/metadata.html#sqlalchemy.schema.Column - Represents a column in a database tbale
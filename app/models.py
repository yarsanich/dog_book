from app import db
from flask_restful import Api, Resource
import sqlalchemy.types as types

ROLE_USER = 0
ROLE_VOLONTEER = 1
ROLE_ADMIN = 2

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(100))
    second_name = db.Column(db.String(100))
    phone_number = db.Column(db.String(100))
    password = db.Column(db.String(100))
    birth_date = db.Column(db.DateTime)
    region = db.Column(db.String(200))
    address = db.Column(db.String(200))
    email = db.Column(db.String(120), unique = True)
    aditional_info = db.Column(db.Text)
    credit_number = db.Column(db.String(200))
    role = db.Column(db.SmallInteger, default = ROLE_USER)

    def __repr__(self):
        return '<User %r %r>' % (self.first_name,self.second_name)

class Status(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    status_title = db.Column(db.String(300))

class Region(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    region_title = db.Column(db.String(300))

class Gender(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    gender_title = db.Column(db.String(300))

class Size(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    size_title = db.Column(db.String(300))

class Dog(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    age = db.Column(db.String(100))
    aditional_info = db.Column(db.Text)
    volnteer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    status = db.Column(db.Integer,db.ForeignKey('status.id'))
    gender = db.Column(db.Integer,db.ForeignKey('gender.id'))
    region = db.Column(db.Integer,db.ForeignKey('region.id'))
    size = db.Column(db.Integer,db.ForeignKey('size.id'))
    def __repr__(self):
        return '<Dog %d>' % (self.id)

from app import db
from flask_restful import Api, Resource
import sqlalchemy.types as types
import json

ROLE_USER = 0
ROLE_VOLONTEER = 1
ROLE_ADMIN = 2

def to_json(model):
    """ Returns a JSON representation of an SQLAlchemy-backed object.
    """
    json1 = {}
    json1['fields'] = {}
    json1['pk'] = getattr(model, 'id')

    for col in model._sa_class_manager.mapper.mapped_table.columns:
        json1['fields'][col.name] = getattr(model, col.name)

    return json.dumps([json1])


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(100))
    second_name = db.Column(db.String(100))
    phone_number = db.Column(db.String(100))
    password = db.Column(db.String(100))
    birth_date = db.Column(db.DateTime,nullable = True)
    region = db.Column(db.Integer,db.ForeignKey('region.id'),nullable = True)
    status = db.Column(db.Integer,db.ForeignKey('volounteer_status.id'),nullable = True)
    address = db.Column(db.String(200),nullable = True)
    email = db.Column(db.String(120), unique = True)
    aditional_info = db.Column(db.Text,nullable = True)
    credit_number = db.Column(db.String(200),nullable = True)
    role = db.Column(db.SmallInteger, default = ROLE_USER)

    def __repr__(self):
        return '<User %r %r>' % (self.first_name,self.second_name)

class Dog_Status(db.Model):
    __tablename__ = 'dog_status'
    id = db.Column(db.Integer,primary_key = True)
    status_title = db.Column(db.String(300))

class Volounteer_Status(db.Model):
    __tablename__ = 'volounteer_status'
    id = db.Column(db.Integer,primary_key = True)
    status_title = db.Column(db.String(300))

class Region(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    region_title = db.Column(db.String(300))

class Gender(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    gender_title = db.Column(db.String(300))

    def __init__(self,  gender_title):
        self.gender_title = gender_title

    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()

    def to_dict(self):
        return {"id":self.id, "gender_title":self.gender_title}

class Size(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    size_title = db.Column(db.String(300))

class Dog(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    age = db.Column(db.String(100),nullable = True)
    aditional_info = db.Column(db.Text,nullable = True)
    volounteer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    status = db.Column(db.Integer,db.ForeignKey('dog_status.id'))
    gender = db.Column(db.Integer,db.ForeignKey('gender.id'))
    region = db.Column(db.Integer,db.ForeignKey('region.id'))
    size = db.Column(db.Integer,db.ForeignKey('size.id'))
    def __repr__(self):
        return '<Dog %d>' % (self.id)

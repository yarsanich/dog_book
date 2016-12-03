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

    def __init__(self,first_name,second_name,phone_number,password,birth_date,region,status,address,email,aditional_info,credit_number,role):
        self.first_name = first_name
        self.second_name = second_name
        self.phone_number = phone_number
        self.password = password
        self.birth_date = birth_date
        self.region = region
        self.status = status
        self.address = address
        self.email = email
        self.aditional_info = aditional_info
        self.credit_number = credit_number
        self.role = role

    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()

    def to_dict(self):
        return {"id":self.id,
                "first_name":self.first_name,
                "second_name":self.second_name,
                "phone_number":selfcredit.phone_number,
                "password":self.password,
                "birth_date":self.birth_date,
                "region":self.region,
                "status":self.status,
                "address":self.address,
                "email":self.email,
                "aditional_info":self.aditional_info,
                "credit_number":self.credit_number,
                "role":self.role,
                }

class Dog_Status(db.Model):
    __tablename__ = 'dog_status'
    id = db.Column(db.Integer,primary_key = True)
    status_title = db.Column(db.String(300))

    def __init__(self,status_title):
        self.status_title = status_title

    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()

    def to_dict(self):
        return {"id":self.id,"status_title":self.status_title}


class Volounteer_Status(db.Model):
    __tablename__ = 'volounteer_status'
    id = db.Column(db.Integer,primary_key = True)
    status_title = db.Column(db.String(300))

    def __init__(self,status_title):
        self.status_title = status_title

    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()

    def to_dict(self):
        return {"id":self.id,"status_title":self.status_title}

class Region(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    region_title = db.Column(db.String(300))

    def __init__(self,status_title):
        self.region_title = region_title

    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()

    def to_dict(self):
        return {"id":self.id,"region_title":self.region_title}

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

    def __init__(self,status_title):
        self.size_title = size_title

    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()

    def to_dict(self):
        return {"id":self.id,"size_title":self.size_title}

class Dog(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    age = db.Column(db.String(100),nullable = True)
    aditional_info = db.Column(db.Text,nullable = True)
    volounteer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    status = db.Column(db.Integer,db.ForeignKey('dog_status.id'))
    gender = db.Column(db.Integer,db.ForeignKey('gender.id'))
    region = db.Column(db.Integer,db.ForeignKey('region.id'))
    size = db.Column(db.Integer,db.ForeignKey('size.id'))

    def __init__(self,age,aditional_info,volnteer_id,status,gender,region,size):
        self.age = age
        self.aditional_info = aditional_info
        self.volnteer_id = volnteer_id
        self.status = status
        self.gender = gender
        self.region = region
        self.size = size

    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()

    def to_dict(self):
        return {"id":self.id,
                "age":self.age,
                "aditional_info":self.aditional_info,
                "volonteer_id":self.volnteer_id,
                "status":self.status,
                "gender":self.gender,
                "region":self.region,
                "size":self.size
                }

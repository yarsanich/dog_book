from app import app, api, db
from flask import request, jsonify, make_response
from flask_restful import Resource, Api, reqparse
import json
from app import models


parser = reqparse.RequestParser()

@app.errorhandler(404)
def e404(er):
    return "404"

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Dogs(Resource):
    def get(self):
        users_query = models.Dog.query.all()
        return users_query

    def put(self):
        return {"todo_id": 1}

class Gender(Resource):
    def get(self, gender_id):
        try:
            users_query = models.Gender.query.filter_by(id=gender_id).first()
            return users_query.to_dict()
        except AttributeError:
            return 404
    def delete(self, gender_id):
        try:
            users_query = models.Gender.query.filter_by(id=gender_id).first()
            db.session.delete(users_query)
            db.session.commit()
            return "200 OK"
        except AttributeError:
            return 404

class Genders(Resource):
    def get(self):
        users_query = models.Gender.query.all()
        res = {}
        for i in range(len(users_query)):
            res[i] = users_query[i].to_dict()
        return res
    def put(self):
        try:
            parser.add_argument('gender_title')
            args = parser.parse_args()
            gender = models.Gender(args['gender_title'])
            gender.add(gender)
            return "200 OK"
        except Exception as e:
            return e

class Dog(Resource):
    def get(self, dog_id):
        try:
            users_query = models.Dog.query.filter_by(id=dog_id).first()
            return users_query.to_dict()
        except AttributeError:
            return 404
    def delete(self, gender_id):
        try:
            users_query = models.Dog.query.filter_by(id=dog_id).first()
            db.session.delete(users_query)
            db.session.commit()
            return "200 OK"
        except AttributeError:
            return 404
class Dogs(Resource):
    def get(self):
        users_query = models.Dog.query.all()
        res = {}
        for i in range(len(users_query)):
            res[i] = users_query[i].to_dict()
        return res
    def put(self):
        try:
            parser.add_argument('age')
            parser.add_argument('aditional_info')
            parser.add_argument('volnteer_id')
            parser.add_argument('gender')
            parser.add_argument('status')
            parser.add_argument('region')
            parser.add_argument('size')
            args = parser.parse_args()
            gender = models.Dog(args['gender_title'])
            gender.add(gender)
            return "200 OK"
        except Exception as e:
            return e

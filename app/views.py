from app import app, api
from flask import request, jsonify, make_response
from flask_restful import Resource, Api, reqparse
import json
from app import models


parser = reqparse.RequestParser()

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Dogs(Resource):
    def get(self):
        users_query = models.Dog.query.all()
        return users_query

    def put(self):
        return {"todo_id": 1}

class Genders(Resource):
    def get(self):
        users_query = models.Gender.query.all()
        res = {}
        for i in range(len(users_query)):
            res[i] = users_query[i].to_dict()
        return res

    def post(self):
        try:
            parser.add_argument('gender_title')
            args = parser.parse_args()
            gender = models.Gender(args['gender_title'])
            gender.add(gender)
            return {"status": 1}
        except Exception as e:
            return e

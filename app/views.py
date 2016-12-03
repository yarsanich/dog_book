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

class Size(Resource):
    def get(self, gender_id):
        try:
            users_query = models.Size.query.filter_by(id=gender_id).first()
            return users_query.to_dict()
        except AttributeError:
            return 404
    def delete(self, gender_id):
        try:
            users_query = models.Size.query.filter_by(id=gender_id).first()
            db.session.delete(users_query)
            db.session.commit()
            return "200 OK"
        except AttributeError:
            return 404

class Sizes(Resource):
    def get(self):
        users_query = models.Size.query.all()
        res = {}
        for i in range(len(users_query)):
            res[i] = users_query[i].to_dict()
        return res
    def put(self):
        try:
            parser.add_argument('size_title')
            args = parser.parse_args()
            gender = models.Size(args['size_title'])
            gender.add(gender)
            return "200 OK"
        except Exception as e:
            return e

class Region(Resource):
    def get(self, gender_id):
        try:
            users_query = models.Region.query.filter_by(id=gender_id).first()
            return users_query.to_dict()
        except AttributeError:
            return 404
    def delete(self, gender_id):
        try:
            users_query = models.Region.query.filter_by(id=gender_id).first()
            db.session.delete(users_query)
            db.session.commit()
            return "200 OK"
        except AttributeError:
            return 404

class Regions(Resource):
    def get(self):
        users_query = models.Region.query.all()
        res = {}
        for i in range(len(users_query)):
            res[i] = users_query[i].to_dict()
        return res
    def put(self):
        try:
            parser.add_argument('region_title')
            args = parser.parse_args()
            gender = models.Region(args['region_title'])
            gender.add(gender)
            return "200 OK"
        except Exception as e:
            return e

class Dog_Status(Resource):
    def get(self, gender_id):
        try:
            users_query = models.Dog_Status.query.filter_by(id=gender_id).first()
            return users_query.to_dict()
        except AttributeError:
            return 404
    def delete(self, gender_id):
        try:
            users_query = models.Dog_Status.query.filter_by(id=gender_id).first()
            db.session.delete(users_query)
            db.session.commit()
            return "200 OK"
        except AttributeError:
            return 404

class Dog_Statuses(Resource):
    def get(self):
        users_query = models.Dog_Status.query.all()
        res = {}
        for i in range(len(users_query)):
            res[i] = users_query[i].to_dict()
        return res
    def put(self):
        try:
            parser.add_argument('status_title')
            args = parser.parse_args()
            gender = models.Dog_Status(args['status_title'])
            gender.add(gender)
            return "200 OK"
        except Exception as e:
            return e

class Volounteer_Status(Resource):
    def get(self, gender_id):
        try:
            users_query = models.Volounteer_Status.query.filter_by(id=gender_id).first()
            return users_query.to_dict()
        except AttributeError:
            return 404
    def delete(self, gender_id):
        try:
            users_query = models.Volounteer_Status.query.filter_by(id=gender_id).first()
            db.session.delete(users_query)
            db.session.commit()
            return "200 OK"
        except AttributeError:
            return 404

class Volounteer_Statuses(Resource):
    def get(self):
        users_query = models.Volounteer_Status.query.all()
        res = {}
        for i in range(len(users_query)):
            res[i] = users_query[i].to_dict()
        return res
    def put(self):
        try:
            parser.add_argument('status_title')
            args = parser.parse_args()
            gender = models.Volounteer_Status(args['status_title'])
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
    def delete(self, dog_id):
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
            parser.add_argument('volounteer_id')
            parser.add_argument('gender')
            parser.add_argument('status')
            parser.add_argument('region')
            parser.add_argument('size')
            args = parser.parse_args()
            gender = models.Dog(args['age'], args['aditional_info'],
                                args['volounteer_id'],args['gender'],args['status'],
                                args['region'], args['size'])
            gender.add(gender)
            return "200 OK"
        except Exception as e:
            return e

    def post(self):
        try:
            parser.add_argument('gender')
            parser.add_argument('status')
            parser.add_argument('region')
            parser.add_argument('size')
            args = parser.parse_args()
            new_args = {}
            for arg in args:
                if args[str(arg)]!=None:
                    new_args[str(arg)] = args[str(arg)]
            print(new_args)
            execute_code = "models.Dog.query.filter_by("
            for arg in new_args:

                execute_code += "%s = %s," % (str(arg),new_args[str(arg)])
            execute_code = execute_code[0:-1] + ").all()"

            print(execute_code)
            dogs_query = eval(execute_code)
            res = {}
            for i in range(len(dogs_query)):
                res[i] = dogs_query[i].to_dict()
            return res,201
        except Exception as e:
            return e

class User(Resource):
    def get(self, user_id):
        try:
            users_query = models.User.query.filter_by(id=user_id).first()
            return users_query.to_dict()
        except AttributeError:
            return 404
    def delete(self, user_id):
        try:
            users_query = models.User.query.filter_by(id=user_id).first()
            db.session.delete(users_query)
            db.session.commit()
            return "200 OK"
        except AttributeError:
            return 404

class Users(Resource):
    def get(self):
        users_query = models.User.query.all()
        res = {}
        for i in range(len(users_query)):
            res[i] = users_query[i].to_dict()
        return res
    def put(self):
        try:
            parser.add_argument('first_name')
            parser.add_argument('second_name')
            parser.add_argument('password')
            parser.add_argument('phone_number')
            parser.add_argument('birth_date')
            parser.add_argument('region')
            parser.add_argument('status')
            parser.add_argument('address')
            parser.add_argument('email')
            parser.add_argument('aditional_info')
            parser.add_argument('credit_number')
            parser.add_argument('role')
            args = parser.parse_args()
            user = models.User(args['first_name'], args['second_name'],
                               args['phone_number'], args['password'], args['birth_date'],
                               args['region'], args['status'], args['address'],
                               args['email'], args['aditional_info'], args['credit_number'], args['role'])
            user.add(user)
            return "200 OK"
        except Exception as e:
            return e

    def post(self):
        try:
            parser.add_argument('status')
            parser.add_argument('region')
            args = parser.parse_args()
            new_args = {}
            for arg in args:
                if args[str(arg)]!=None:
                    new_args[str(arg)] = args[str(arg)]
            print(new_args)
            execute_code = "models.User.query.filter_by("
            for arg in new_args:

                execute_code += "%s = %s," % (str(arg),new_args[str(arg)])
            execute_code = execute_code[0:-1] + ").all()"

            print(execute_code)
            users_query = eval(execute_code)
            res = {}
            for i in range(len(users_query)):
                res[i] = users_query[i].to_dict()
            return res,201
        except Exception as e:
            return e

import json
import werkzeug
import os
from app import app, api, db
from flask import request, jsonify, make_response,redirect,url_for,send_from_directory,abort,g,session
from werkzeug.utils import secure_filename
from flask_restful import Resource, Api, reqparse
from config import ALLOWED_EXTENSIONS,auth
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)
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

    #@auth.login_required
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
        res = []
        for i in range(len(users_query)):
            res.append(users_query[i].to_dict())
        return res
    #@auth.login_required
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
    #@auth.login_required
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
        res = []
        for i in range(len(users_query)):
            res.append(users_query[i].to_dict())
        return res
    #@auth.login_required
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
    #@auth.login_required
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
        res = []
        for i in range(len(users_query)):
            res.append(users_query[i].to_dict())
        return res
    #@auth.login_required
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
    #@auth.login_required
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
        res = []
        for i in range(len(users_query)):
            res.append(users_query[i].to_dict())
        return res

    #@auth.login_required
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
    #@auth.login_required
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
        res = []
        for i in range(len(users_query)):
            res.append(users_query[i].to_dict())
        return res
    #@auth.login_required
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
    #@auth.login_required
    def put(self, dog_id):
        try:
            parser.add_argument('age')
            parser.add_argument('aditional_info')
            parser.add_argument('volounteer_id')
            parser.add_argument('gender')
            parser.add_argument('status')
            parser.add_argument('region')
            parser.add_argument('size')
            args = parser.parse_args()
            session = db.session()
            u = session.query(models.Dog).filter_by(id=dog_id)
            for arg in args:
                if (args[str(arg)] != None):
                    u.update({"%s" % (str(arg)):args[str(arg)]})
            session.commit()
            return "200 OK"
        except Exception as e:
            return e
    #@auth.login_required
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
        res = []
        for i in range(len(users_query)):
            res.append(users_query[i].to_dict())
        return res
    def put(self):
        parser.add_argument('age')
        parser.add_argument('aditional_info')
        parser.add_argument('volounteer_id')
        parser.add_argument('gender')
        parser.add_argument('status')
        parser.add_argument('region')
        parser.add_argument('size')
        args = parser.parse_args()
        if args["volounteer_id"] == None:
            abort(400,{"errors":"volounteer undefined"})
        elif args["status"] == None:
            abort(400,{"errors":"status undefined"})
        elif args["region"] == None:
            abort(400,{"errors":"region undefined"})
        elif args["size"] == None:
            abort(400,{"errors":"size undefined"})
        else:
            gender = models.Dog(args['age'], args['aditional_info'],
                                args['volounteer_id'],args['gender'],args['status'],
                                args['region'], args['size'])
            gender.add(gender)
            return "200 OK"

    def post(self):
        try:
            parser.add_argument('gender')
            parser.add_argument('status')
            parser.add_argument('region')
            parser.add_argument('size')
            parser.add_argument('age')
            parser.add_argument('volounteer_id')
            args = parser.parse_args()
            new_args = {}
            for arg in args:
                if args[str(arg)]!=None:
                    new_args[str(arg)] = args[str(arg)]
            execute_code = "models.Dog.query.filter_by("
            for arg in new_args:
                execute_code += "%s = %s," % (str(arg),new_args[str(arg)])
            if len(new_args)>0:
                execute_code = execute_code[0:-1] + ").all()"
            else:
                execute_code = "models.Dog.query.all()"

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
    #@auth.login_required
    def delete(self, user_id):
        try:
            users_query = models.User.query.filter_by(id=user_id).first()
            db.session.delete(users_query)
            db.session.commit()
            return "200 OK"
        except AttributeError:
            return 404
    def put(self, user_id):
        try:
            parser.add_argument('first_name')
            parser.add_argument('second_name')
            parser.add_argument('password')
            parser.add_argument('phone_number')
            parser.add_argument('birth_date')
            parser.add_argument('region')
            parser.add_argument('status')
            sadasparser.add_argument('address')
            parser.add_argument('email')
            parser.add_argument('aditional_info')
            parser.add_argument('credit_number')
            parser.add_argument('role')
            args = parser.parse_args()
            print(args)
            session = db.session()
            u = session.query(models.User).filter_by(id=user_id)
            for arg in args:
                if (args[str(arg)] != None):
                    u.update({"%s" % (str(arg)):args[str(arg)]})
            session.commit()
            return "200 OK"
        except Exception as e:
            return e
class Users(Resource):
    #@auth.login_required
    def get(self):
        users_query = models.User.query.all()
        res = []
        for i in range(len(users_query)):
            res.append(users_query[i].to_dict())
        return res
    #@auth.login_required
    def put(self):
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
        if args["first_name"] == None:
            abort(400,{"errors":"first_name undefined"})
        elif args["second_name"] == None:
            abort(400,{"errors":"second undefined"})
        elif args["password"] == None:
            abort(400,{"errors":"password undefined"})
        elif args["phone_number"] == None:
            abort(400,{"errors":"phone_number undefined"})
        else:
            if args['email'] is None or args['password'] is None:
                abort(400)    # missing arguments
            if models.User.query.filter_by(email=args['email']).first() is not None:
                abort(400)    # existing user
            user = models.User(args['first_name'], args['second_name'],
                               args['phone_number'], args['birth_date'],
                               args['region'], args['status'], args['address'],
                               args['email'], args['aditional_info'], args['credit_number'], args['role'])
            user.hash_password(args["password"])
            user.add(user)
            return "200 OK"
    #@auth.login_required
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

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/api/dogs/<dog_id>/photo', methods=['POST','GET'])
def file_upload_dog(dog_id):
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            app.logger.debug("NO SELECTED FILE")
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            app.logger.debug("NO SELECTED FILE")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            session = db.session()
            u = session.query(models.Dog).get(dog_id)
            u.photo = filename
            session.commit()
    return '''
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

@app.route('/api/users/<user_id>/photo', methods=['POST'])
def file_upload_user(user_id):
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            app.logger.debug("NO SELECTED FILE")
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            app.logger.debug("NO SELECTED FILE")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            photo = models.Photo(user_id,filename)
            photo.add(photo)

class user_photos(Resource):
    def get(self,user_id):
        photo_query = models.Photo.query.filter_by(user = user_id).first()
        if (photo_query!= None):
            res = []
            for i in range(len(photo_query)):
                res.append(photo_query[i].to_dict())
            return res
        else:
            return {"error":"no pohotos"}

class dog_photos(Resource):
    def get(self,dog_id):
        photo_query = models.Photo.query.filter_by(dog = dog_id).first()
        if photo_query!=None:
            res = []
            for i in range(len(photo_query)):
                res.append(photo_query[i].to_dict())
            return res
        else:
            return {"error":"no pohotos"}


@app.route('/photos/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@auth.verify_password
def verify_password(email_or_token, password):
    # first try to authenticate by token
    user = models.User.verify_auth_token(email_or_token)
    if not user:
        # try to authenticate with email/password
        user = models.User.query.filter_by(email=email_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True

def before_request():
    print current_user
    g.user = current_user

@app.route('/api/token')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token(600)
    return jsonify({'token': token.decode('ascii'), 'duration': 600})

@app.route('/api/resource')
@auth.login_required
def get_resource():
    return jsonify({'data': 'Hello, %s!' % g.user.email})

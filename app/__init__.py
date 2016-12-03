from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
api = Api(app)
from app import models, views

api.add_resource(views.HelloWorld, '/')
api.add_resource(views.Dogs, '/api/dogs/')
api.add_resource(views.Genders, '/api/genders/')
#api.add_resource(views.Dog, '/api/dogs/<int:dog_id>')
#api.add_resource(views.User, '/api/users/<int:user_id>')
#api.add_resource(views.Users, '/api/users/')

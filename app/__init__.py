from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
api = Api(app)
from app import models, views

api.add_resource(views.HelloWorld, '/')

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
api.add_resource(views.Dog, '/api/dogs/<int:dog_id>')

api.add_resource(views.Users, '/api/users/')
api.add_resource(views.User, '/api/users/<int:user_id>')

api.add_resource(views.Genders, '/api/genders/')
api.add_resource(views.Gender, '/api/genders/<int:gender_id>')

api.add_resource(views.Dog_Statuses, '/api/dogs/statuses/')
api.add_resource(views.Dog_Status, '/api/dogs/statuses/<int:status_id>')

api.add_resource(views.Volounteer_Statuses, '/api/users/statuses/')
api.add_resource(views.Volounteer_Status, '/api/users/statuses/<int:gender_id>')

api.add_resource(views.Regions, '/api/regions/')
api.add_resource(views.Region, '/api/regions/<int:regions_id>')

api.add_resource(views.Sizes, '/api/sizes/')
api.add_resource(views.Size, '/api/sizes/<int:sizes_id>')

api.add_resource(views.user_photos, '/api/users/<int:user_id>/photo')

#api.add_resource(views.Dog, '/api/dogs/<int:dog_id>')
#api.add_resource(views.User, '/api/users/<int:user_id>')
#api.add_resource(views.Users, '/api/users/')

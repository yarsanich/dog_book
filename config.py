import os
from werkzeug.utils import secure_filename
from os.path import join, dirname, realpath
from flask.ext.httpauth import HTTPBasicAuth

basedir = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = (os.path.join(basedir, "images"))
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


auth = HTTPBasicAuth()

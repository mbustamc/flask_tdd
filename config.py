#config.py

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    UPLOAD_FOLDER = os.path.join(basedir, 'uploads')
    ALLOWED_EXTENSIONS = os.environ.get('ALLOWED_EXTENSIONS')
    UPLOADS_DEFAULT_DEST =  os.path.join(basedir, 'project/static/uploads')
    UPLOADED_IMAGES_DEST =  os.path.join(basedir, 'project/static/uploads')

from project import db, create_app
from project.models import *

db.create_all(app=create_app())
#create database and tables




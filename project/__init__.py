import os

from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy
from config import Config

from flask_migrate import Migrate
from flask_admin import Admin
from flask_uploads import UploadSet, IMAGES, configure_uploads


import os
basedir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy()
migrate = Migrate()
admin = Admin(name='Admin', template_mode='bootstrap3')
photos = UploadSet('photos', IMAGES)


#inicialize


def create_app():

	application = Flask(__name__)
	application.config.from_object(Config)

	db.init_app(application)
	migrate.init_app(application, db)
	admin.init_app(application)
	
	configure_uploads(application, photos)

	from project.models.bp_catalogo import Productor, Rubro, Producto
	from project.models.bp_upload import Imagen

	from project.bp_admin import bp as bp_admin
	application.register_blueprint(bp_admin, url_prefix='/admin')


	from project.bp_catalogo import bp as bp_catalogo
	application.register_blueprint(bp_catalogo, url_prefix='/catalogo')

	from project.bp_upload import bp as bp_upload
	application.register_blueprint(bp_upload, url_prefix='/upload')

	return application




import os

from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy
from config import Config

from flask_admin import Admin


db = SQLAlchemy()
admin = Admin(name='Admin', template_mode='bootstrap3')
#inicialize


def create_app():

	application = Flask(__name__)
	application.config.from_object(Config)

	db.init_app(application)
	admin.init_app(application)


	from project.models import Productor, Rubro

	from project.bp_admin import bp as bp_admin
	application.register_blueprint(bp_admin, url_prefix='/admin')


	@application.route('/')
	def index():
	    """Searches the database for entries, then displays them."""
	    entries = db.session.query(Rubro)
	    return render_template('index.html', entries=entries)

	return application




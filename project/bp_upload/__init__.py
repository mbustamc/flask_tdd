#upload/__init__.py

from flask import Blueprint

bp = Blueprint('bp_upload', __name__)

from project.bp_upload import routes
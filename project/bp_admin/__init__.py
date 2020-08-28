#admin/__init__.py

from flask import Blueprint

bp = Blueprint('bp_admin', __name__)

from . import routes
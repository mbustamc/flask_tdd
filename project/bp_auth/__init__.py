#auth/__init__.py

from flask import Blueprint

bp = Blueprint('bp_auth', __name__)

from project.bp_auth import routes
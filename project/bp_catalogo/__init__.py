# project/catalogo/__init__.py

from flask import Blueprint

bp = Blueprint('bp_catalogo', __name__)

from project.bp_catalogo import routes
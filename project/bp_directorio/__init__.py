# project/catalogo/__init__.py

from flask import Blueprint

bp = Blueprint('bp_directorio', __name__)

from project.bp_directorio import routes
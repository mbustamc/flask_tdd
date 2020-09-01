from flask import Flask, render_template

from project import db
from project.models.bp_catalogo import *
from project.bp_catalogo import bp


@bp.route('/')
def index():
	"""Searches the database for entries, then displays them."""
	entries = db.session.query(Rubro).all()
	#entries = db.session.query(Rubro)
	return render_template('bp_catalogo/index.html', entries=entries)

@bp.route('/rubro/<id_rubro>')
def index_rubro(id_rubro):
	"""Searches the database for entries, then displays them."""
	entries = db.session.query(Productor).join(Productor, Producto.productores).join(Rubro, Producto.rubros).filter(Rubro.id==id_rubro).all()
	nombre_rubro = db.session.query(Rubro.nombre).filter(Rubro.id==id_rubro).first()
	return render_template('bp_catalogo/index_rubro.html', nombre_rubro= nombre_rubro, entries=entries)

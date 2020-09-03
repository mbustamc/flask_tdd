from flask import Flask, render_template, request, flash

from project import db
from project.models.bp_catalogo import *
from project.bp_catalogo import bp
from .forms import ElegirRubroForm



@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    form = ElegirRubroForm()
    entries = db.session.query(Rubro).all()
    form.rubro.choices = [(rubro.id, rubro.nombre) for rubro in Rubro.query.all()]
    if request.method == "POST":
    	id_rubro = request.form['rubro']
    	seleccionado = db.session.query(Productor).join(Productor, Producto.productores).join(Rubro, Producto.rubros).filter(Rubro.id==id_rubro).all()
    	return render_template('bp_catalogo/index.html', entries=entries, form=form ,seleccionado=seleccionado)

    return render_template('bp_catalogo/index.html',entries=entries, form= form)

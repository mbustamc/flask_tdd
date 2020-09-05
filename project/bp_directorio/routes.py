from flask import Flask, render_template, request, flash

from project import db
from project.models.bp_directorio import *
from project.bp_directorio import bp
from .forms import ElegirRubroForm



@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    form = ElegirRubroForm()
    entries = db.session.query(Productor).all()
    form.rubro.choices = [(rubro.id, rubro.nombre) for rubro in Rubro.query.all()]
    form.rubro.choices.insert(0,(0, 'Selecciona el rubro'))
    if request.method == "POST":
    	id_rubro = request.form['rubro']
    	entries = db.session.query(Productor).join(Productor, Producto.productores).join(Rubro, Producto.rubros).filter(Rubro.id==id_rubro).all()
    	return render_template('bp_directorio/index.html', entries=entries, form=form)

    return render_template('bp_directorio/index.html',entries=entries, form= form)

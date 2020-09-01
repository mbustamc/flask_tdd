from datetime import datetime
from flask import render_template, flash, redirect, url_for, session, request

from project.bp_upload import bp
from project import db

from project.models.bp_upload import Imagen
from project.models.bp_catalogo import Productor

from project import photos
from .forms import *



@bp.route('/', methods=['GET', 'POST'])
def index():
    form = UploadForm()
    form.productor.choices = [(productor.id, productor.nombre_fantasia) for productor in Productor.query.order_by(Productor.nombre_fantasia).all()]
    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        file_url = photos.url(filename)

        image = Imagen()
        image.name = filename
        image.path = file_url
        image.productor_id = request.form['productor']
        db.session.add(image)
        db.session.commit()
        flash('New Image added!')
        return redirect(url_for('bp_catalogo.index'))
    else:
        file_url = None
    return render_template('bp_upload/index.html', form=form, file_url=file_url)

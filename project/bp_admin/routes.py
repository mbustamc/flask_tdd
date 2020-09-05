	
#app/bp_admin/views.py
from flask import Blueprint, flash, redirect, render_template, request, url_for, current_app, session
from flask_login import login_required, login_user, logout_user, current_user

from flask_admin import  BaseView, expose, form
from flask_admin.contrib.sqla import ModelView


from project import admin
from project import db

from project.models.bp_directorio import *
from project.models.bp_auth import *

from project.bp_admin import bp


class RestrictedView(ModelView):
    page_size = 50


    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('login', next=request.url))


admin.add_view(RestrictedView(User, db.session))
admin.add_view(RestrictedView(Rubro, db.session))
admin.add_view(RestrictedView(Productor, db.session))

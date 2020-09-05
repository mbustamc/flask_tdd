from datetime import datetime
from flask import render_template, flash, redirect, url_for, session, request
from flask_login import login_required, current_user, login_user, logout_user
from werkzeug.urls import url_parse

from project.bp_auth import bp
from project import db

from project.models.bp_auth import User

from .forms import LoginForm, RegistrationForm, EditProfileForm

from functools import wraps

def admin_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
    	#if current_user.role not in ([Role.admin,]):
    	if current_user.is_authenticated and not current_user.is_admin:
    		flash('Insufficient privilige for user'.format(current_user.username))
    		next_page = request.args.get('next')
    		if not next_page:
    			next_page = url_for('bp_directorio.index')
    		return redirect(next_page)
    		#return redirect(url_for('bp_directorio.index'))
    	return f(*args, **kwargs)
    return decorator


@bp.before_request
def before_request():
	if current_user.is_authenticated:
		current_user.last_seen = datetime.utcnow()
		db.session.commit()

@bp.route("/")
@login_required
def index():
	return redirect(url_for('bp_directorio.index'))


@bp.route('/login', methods=['GET', 'POST'])
def login():
	title='Sign In'
	if current_user.is_authenticated:
		return redirect(url_for('bp_directorio.index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Invalid username or password')
			return redirect(url_for('bp_auth.login'))
		remember_me = False
		#remember_me=form.remember_me.data
		login_user(user, remember=remember_me)
		next_page = request.args.get('next')
		if not next_page:
			next_page = url_for('bp_directorio.index')
		return redirect(next_page)
	return render_template('bp_auth/login.html', title=title, form=form)



@bp.route('/logout')
def logout():
    logout_user()
    session.clear()
    return redirect(url_for('bp_directorio.index'))


@bp.route('/register', methods=['GET', 'POST'])
def register():
	title='Register'
	if current_user.is_authenticated:
		return redirect(url_for('bp_directorio.index'))
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(username=form.username.data, email=form.email.data)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('Congratulations, you are now a registered user!')
		return redirect(url_for('bp_auth.login'))
	return render_template('bp_auth/register.html', title=title, form=form)


@bp.route('/user/<username>')
@login_required
def user(username):
	title='Ver perfil'
	user = User.query.filter_by(username=username).first_or_404()
	return render_template('bp_auth/user.html', title=title, user=user)



@bp.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
	title='Actualiza tu perfil'
	form = EditProfileForm(current_user.username)
	if form.validate_on_submit():
		current_user.username = form.username.data
		current_user.about_me = form.about_me.data
		db.session.commit()
		flash('Your changes have been saved.')
		return redirect(url_for('bp_auth.user', username=current_user.username))
	elif request.method == 'GET':
		form.username.data = current_user.username
		form.about_me.data = current_user.about_me
	return render_template('bp_auth/edit_profile.html', title=title,
		form=form)
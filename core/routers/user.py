from flask import Blueprint, render_template, session, url_for, redirect
from werkzeug.security import generate_password_hash

from core.init.app import login_manager, db
from core.database import User, Notes
from core.forms import LoginForm, RegistrationForm
from core.validators import (
    validate_email,
    validate_username,
    validate_password
)


user_router = Blueprint('user', __name__)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@user_router.route('/')
def home():
    notes = Notes().query.all()
    return render_template('home/index.html', notes=notes)


@user_router.route('/auth', methods=['POST', 'GET'])
def auth():
    register_form = RegistrationForm()
    login_form = LoginForm()

    if register_form.is_submitted():
        if not validate_email(register_form.email):
            if not validate_username(register_form.username):
                username = register_form.username.data
                email = register_form.email.data
                password = register_form.password.data
                user = User(
                    username=username,
                    email=email,
                    password=generate_password_hash(password)
                )
                db.session.add(user)
                db.session.commit()
                db.session.close()
                session['username'] = username

    if login_form.is_submitted():
        if validate_username(login_form.username):
            if validate_password(login_form.username, login_form.password):
                username = login_form.username.data
                return redirect(url_for('user.home', username=username))

    return render_template(
        'auth.html',
        register_form=register_form,
        login_form=login_form
    )



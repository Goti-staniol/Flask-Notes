from flask import Blueprint, render_template

from core.init.app import login_manager
from core.database import User, Notes


home_router = Blueprint('home', __name__)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@home_router.route('/')
def home():
    notes = Notes().query.all()
    return render_template('home/index.html', notes=notes)


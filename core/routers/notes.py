from flask import Blueprint, render_template


notes_router = Blueprint('notes', __name__)


@notes_router.route('/add-note')
def add_note_menu():
    return render_template('notes/index.html')
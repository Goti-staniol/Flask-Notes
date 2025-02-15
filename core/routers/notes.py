from flask import Blueprint, render_template, request, jsonify


notes_router = Blueprint('notes', __name__)


@notes_router.route('/add-note')
def add_note_menu():
    return render_template('notes/index.html')


@notes_router.route('/save_note', methods=['POST'])
def save_note():
    data = request.json

    title = data.get('title')
    description = data.get('description')
    photos = data.get('photos', [])

    for photo in photos:
        photo_name = photo['name']
        photo_data = photo['data']

    print(title, description, photo_name)

    return jsonify(
        {"status": "success", "note_id": 1, "photo_urls": photo_data})

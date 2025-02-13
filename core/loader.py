from flask import Blueprint, send_from_directory


loader_router = Blueprint('loader', __name__)


@loader_router.route("/static/<path:filename>")
def load_style(filename):
    return send_from_directory("core/static", filename)


@loader_router.route("/static/<path:filename>")
def load_scripts(filename):
    return send_from_directory("core/scripts", filename)
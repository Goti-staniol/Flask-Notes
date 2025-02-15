import os


class Config:
    SECRET_KEY = os.urandom(24).hex()
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    UPLOAD_FOLDER = os.path.abspath('core/static/uploads')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

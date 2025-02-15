from werkzeug.security import check_password_hash
from wtforms import (
    StringField,
    PasswordField
)

from core.database import User


def validate_username(username: StringField) -> bool:
    user = User.query.filter_by(username=username.data).first()
    if user:
        return True
    return False

def validate_email(email: StringField) -> bool:
    user = User.query.filter_by(email=email.data).first()
    if user:
        return  True
    return False

def validate_password(username: StringField, password: PasswordField):
    user = User.query.filter_by(username=username.data).first()
    if check_password_hash(user.password, password.data):
        return True
    return False
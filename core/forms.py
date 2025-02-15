from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed

from wtforms.validators import DataRequired, Email
from wtforms import (
    StringField,
    TextAreaField,
    SubmitField,
    PasswordField
)


class LoginForm(FlaskForm):
    username = StringField(label='username', validators=[DataRequired()])
    password = PasswordField(label='password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    username = StringField(label='username', validators=[DataRequired()])
    email = StringField(label='email', validators=[DataRequired(), Email()])
    password = PasswordField(label='password', validators=[DataRequired()])
    submit = SubmitField('Registration')


class NoteForm(FlaskForm):
    title = StringField(label='title', validators=[DataRequired()])
    description = TextAreaField(label='description')
    photo = FileField(
        'Photo',
        validators=[
            FileAllowed(
                upload_set=['png', 'jpeg', 'jpg'],
                message='Только Фотографии!'
            )
        ]
    )
    submit = SubmitField('Сохранить')
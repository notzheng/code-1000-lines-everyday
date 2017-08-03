from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, BooleanField, ValidationError, TextAreaField, FileField, SelectField)
from wtforms.validators import (DataRequired, NumberRange, Email, EqualTo, Length, Optional, AnyOf)


class LoginForm():
    username = StringField('Username',
                           validators=[DataRequired(), Length(max=30, message='The length must unser 30')])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me', default=False)

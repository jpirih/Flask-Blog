from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired( message='Vnos tega polja je obvezen')])
    password = PasswordField('Password', validators=[DataRequired(message='Vnos tega polja je obvezen')])


class RegisterForm(Form):
    username = StringField('username', validators=[DataRequired(message='Vnos tega polja je obvezen'), Length(min=3, max=25)])
    email = StringField('email', validators=[DataRequired(message='Vnos tega polja je obvezen'), Length(min=6, max=40), Email(message=None)])
    password = PasswordField('password', validators=[DataRequired(message='Vnos tega polja je obvezen'), Length(min=6, max=25)])
    confirm = PasswordField('Repeat password', validators=[DataRequired(message='Vnos tega polja je obvezen'), EqualTo('password', message="Gesli se morata obvzno ujemati")])

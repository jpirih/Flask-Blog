from flask_wtf import Form
from wtforms import StringField, TextAreaField,SelectMultipleField
from wtforms.validators import DataRequired


class CreatePostForm(Form):
    title = StringField('title', validators=[DataRequired(message='Vnos tega polja je obvezen')])
    description = TextAreaField('description', validators=[DataRequired(message='Vnos tega polja je obvezen')])
    categories = SelectMultipleField('categories')

class CommentForm(Form):
    title = StringField('title', validators=[DataRequired(message='Vnos tega polja je obvezen')])
    content = TextAreaField('content', validators=[DataRequired(message='Vnos tega polja je obvezen')])
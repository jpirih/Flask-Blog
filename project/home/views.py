from flask import render_template, request, redirect, url_for, session, flash, Blueprint
from project import db
from project.models import BlogPost
from urllib import urlopen
import json



# blueprint config
home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)


# routing
@home_blueprint.route('/')
def home():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Cerkno,uk&units=metric&appid=425d08d39ad4a87c17bcb351795ba4c3'
    result = urlopen(url).read()
    weather = json.loads(result)
    posts = db.session.query(BlogPost).order_by('id desc').limit(3).all()
    return render_template('index.html', posts=posts, weather=weather)


@home_blueprint.route('/welcome')
def welcome():
    return render_template('welcome.html')

@home_blueprint.route('/contact')
def contact():
	return render_template('contact.html')








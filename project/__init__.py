
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from flask.ext.login import LoginManager, current_user

app = Flask(__name__)
# bcrypt enabled
bcrypt = Bcrypt(app)
# flask login enabled
login_manager = LoginManager()
login_manager.init_app(app)


#config
app.config.from_object('config.DevConfig')

# SQLAlchemy object - povezava z bazo
db = SQLAlchemy(app)

from models import *
from project.users.views import users_blueprint
from project.home.views import home_blueprint
from project.blog.views import blog_blueprint

app.register_blueprint(users_blueprint)
app.register_blueprint(home_blueprint)
app.register_blueprint(blog_blueprint)

# katera funkcija se ukvarja z logiranjem uporabnikov flask-login
from models import User
login_manager.login_view = 'users.login'
login_manager.login_message = 'Za ogled te strani je obvezna prijava.'

# pridobi uporabnika iz baze in shrani v cookie flask -login obvezno
@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()
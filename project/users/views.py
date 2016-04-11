from flask import flash, redirect, url_for, render_template, request, session, Blueprint
from flask.ext.login import login_user, login_required, logout_user, current_user
from forms import LoginForm, RegisterForm
from project.models import User, bcrypt
from project import db

# config blueprint struktura projekta
users_blueprint = Blueprint(
    'users', __name__,
    template_folder='templates'
)


# routes
@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(name=request.form['username']).first()
            if user is not None and bcrypt.check_password_hash(user.password, request.form['password']):
                login_user(user)
                flash("Prijava uspela pijavljen is kot {}".format(current_user.name))
                return redirect(url_for('blog.blog_home'))
            error = 'Napaka: Nepravilen uporabnik oziroma geslo. Prosim poskusi znova'
        else:
            return render_template('login.html', form=form, error=error)

    return render_template('login.html', form=form, error=error)


@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # shrani podatke v bazo
            user = User(
                name=form.username.data,
                email=form.email.data,
                password=form.password.data
            )
            db.session.add(user)
            db. session.commit()

            # avtomatsko prijavi uporabnika
            login_user(user)
            flash('Registracija uporabnika je uspela. Prijavljen si kot {} '.format(current_user.name))
            return redirect(url_for('blog.blog_home'))

    return render_template('register.html', form=form)


# odjavi uporabnika session.pop vzame logged_in True in zamenja z None
# izbris secret key - cookie
@users_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Odjava je uspela! ")
    return redirect(url_for('home.welcome'))


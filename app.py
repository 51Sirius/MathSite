from flask import Flask, render_template, request, redirect, url_for, abort
from flask_migrate import Migrate
from flask_wtf import form
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
import datetime
import locale
from os import environ
from forms import LoginForm, Registration, Answer
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import Users, db
from flask_login import LoginManager, login_user, logout_user, current_user, login_required

app = Flask(__name__)
locale.setlocale(locale.LC_ALL, '')
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)
login = LoginManager(app)


@login.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


@app.route('/')
def main_page():
    return render_template('index.html', title='MathTR')


@app.route('/play')
def play_menu():
    return render_template('play.html', title='Game')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    forms = LoginForm()
    if forms.validate_on_submit():
        nick = forms.username.data
        password = forms.password.data
        user = Users.query.filter_by(username=nick).first()
        if not (user and user.check_password(password)):
            abort(403)
        login_user(user, remember=forms.remember_me)
        return redirect(url_for('main_page'))
    return render_template('login.html', title='Login', form=forms)


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    register_form = Registration()
    if register_form.validate_on_submit():
        email = register_form.mail.data
        name = register_form.nickname.data
        password = register_form.password.data
        existing_user = Users.query.filter_by(mail=email).first()
        if existing_user:
            abort(400)
        user = Users(username=name, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main_page'))
    return render_template('registration.html', form=register_form, title='Registration')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main_page'))


if __name__ == '__main__':
    app.run()

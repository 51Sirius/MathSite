from flask import Flask, render_template, request, redirect, url_for, abort
from flask_migrate import Migrate
from flask_wtf import form
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
import datetime
import locale
from os import environ
from forms import LoginForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/')
def main_page():
    return render_template('index.html', title='MathTR')


@app.route('/play')
def play_menu():
    return render_template('play.html', title='Game')


@app.route('/login')
def login():
    forms = LoginForm()
    if forms.validate_on_submit():
        nick = forms.mail_or_name.data
        password = forms.password.data
        user = Users.query.filter_by(mail=nick).first()
        if not (user and user.check_password(password)):
            abort(403)
        login_user(user, remember=forms.remember_me)
        return redirect(url_for('main_page'))
    return render_template('login.html', title='Login', form=forms)


if __name__ == '__main__':
    app.run()

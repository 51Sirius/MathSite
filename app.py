from flask import Flask, render_template, request, redirect, url_for, abort
from flask_migrate import Migrate
from flask_wtf import form
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
import datetime
import locale
from os import environ
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'


@app.route('/')
def main_page():
    return render_template('index.html', title='MathTR')


@app.route('/play')
def play_menu():
    return render_template('play.html', title='Game')


@app.route('/login')
def login():
    forms = LoginForm()
    return render_template('login.html', title='Game', form=forms)


if __name__ == '__main__':
    app.run()

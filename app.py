from flask import Flask, render_template, request, redirect, url_for, abort

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html', title='MathTR')


@app.route('/play')
def play_menu():
    return render_template('')


if __name__ == '__main__':
    app.run()

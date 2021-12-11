from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('template.html')


@app.route('/menu')
def menu():
    return render_template('menu_page.html')

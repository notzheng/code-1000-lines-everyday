from flask import Flask, render_template
from flask import request
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

if __name__ == '__main__':
    app.run()

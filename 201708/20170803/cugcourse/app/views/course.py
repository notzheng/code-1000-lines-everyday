from flask import render_template, Blueprint

course = Blueprint('course', __name__)


@course.route('/')
def index():
    return 'Courses!'

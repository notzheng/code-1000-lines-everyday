from flask import Blueprint, request, redirect, url_for, render_template, flash, abort, jsonify
from flask_login import login_user, login_required, current_user, logout_user

homepage = Blueprint('homepage', __name__)


@homepage.route('/')
def index():
    return render_template('index.html')


@homepage.route('/signin',methods=['POST','GET'])
def signin():
    return render_template('signin/signin.html')
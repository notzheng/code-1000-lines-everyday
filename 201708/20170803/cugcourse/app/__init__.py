"""
    CUG courses


"""

import os
from flask import Flask, request, url_for, render_template, Blueprint
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user, user_logged_in, user_loaded_from_cookie
from config import config

# app = Flask(__name__)

# db = SQLAlchemy()

app = Flask(__name__)
app.config.from_object(config['default'])

from app.views import *

app.register_blueprint(homepage,url_prefix='')
app.register_blueprint(course,url_prefix='/course')

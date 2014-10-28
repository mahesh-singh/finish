import os
import sys

from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

app = Flask(__name__)

app.config.from_object('config.DevConfig')

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

config = app.config


from app.users.views import mod as usersModule
app.register_blueprint(usersModule)

from app.public.views import mod as publicModule
app.register_blueprint(publicModule)

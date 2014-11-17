import urllib
import urllib2
import os
import sys

from flask import Flask, render_template, g, url_for, request
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager,  current_user
from flask.ext import restful

app = Flask(__name__)
api = restful.Api(app)

app.config.from_object('config.DevConfig')

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

config = app.config

@app.before_request
def before_request():
	g.user = current_user
	if not current_user.is_authenticated():
		print('current_user is  None')
		params = {
		'response_type' : 'code',
		'client_id' : config['GOOGLE_API_CLIENT_ID'],
		'redirect_uri' : url_for('users.auth', _external = True),
		'scope' : config['GOOGLE_API_SCOPE'],
		'state' : request.args.get('next')
		}

		url = config['GOOGLE_OAUTH2_URL'] + 'auth?' + urllib.urlencode(params)
		g.login_url = url
		

from app.users.views import mod as usersModule
app.register_blueprint(usersModule)

from app.tasks.views import mod as tasksModule
app.register_blueprint(tasksModule)

from app.public.views import mod as publicModule
app.register_blueprint(publicModule)

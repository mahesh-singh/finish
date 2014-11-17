import urllib
import urllib2
import json

from flask import Blueprint, request, render_template, redirect, url_for
from flask.ext.login import login_user, login_required

from app import db
from app.users.models import User
from app import config
from app import login_manager
mod = Blueprint('users', __name__, url_prefix='/users')


@mod.route('/')
@login_required
def home():
	return render_template('users/index.html')


@mod.route('/login')
def login():
	params = {
		'response_type' : 'code',
		'client_id' : config['GOOGLE_API_CLIENT_ID'],
		'redirect_uri' : url_for('users.auth', _external = True),
		'scope' : config['GOOGLE_API_SCOPE'],
		'state' : request.args.get('next')
	}

	url = config['GOOGLE_OAUTH2_URL'] + 'auth?' + urllib.urlencode(params)
	context = {'login_url' : url}
	return render_template('users/login.html', **context)


@mod.route('/auth')
def auth():
	response = _get_token()
	data = _get_data(response)

	user = User.get_or_create(data)
	login_user(user)
	return redirect(request.args.get('next') or  url_for('users.home'))

#private method
def _get_token():
	params = {
	'code': request.args.get('code'),
	'client_id': config['GOOGLE_API_CLIENT_ID'],
	'client_secret': config['GOOGLE_API_CLIENT_SECRET'],
	'redirect_uri': url_for('users.auth', _external=True),
	'grant_type': 'authorization_code',
	}
	payload = urllib.urlencode(params)
	url = config['GOOGLE_OAUTH2_URL'] + 'token'
	req = urllib2.Request(url, payload)  # must be POST
	return json.loads(urllib2.urlopen(req).read())

def _get_data(response):
	params = {
	'access_token': response['access_token'],
	}
	payload = urllib.urlencode(params)
	url = config['GOOGLE_API_URL'] + 'userinfo?' + payload

	req = urllib2.Request(url)  # must be GET

	return json.loads(urllib2.urlopen(req).read())

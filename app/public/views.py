from flask import Blueprint, request, render_template, redirect, url_for

from app import config

mod = Blueprint('public', __name__, url_prefix='/')


@mod.route('/')
def home():
	return render_template('public/index.html')
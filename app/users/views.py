from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

from app import db
from app.users.models import User

mod = Blueprint('users', __name__, url_prefix='/users')
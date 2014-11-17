from flask import Blueprint
from app.tasks.models import Task, SubTask 

mod = Blueprint('tasks', __name__, url_prefix='/tasks')
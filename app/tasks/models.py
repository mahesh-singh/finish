from app import db
from app.tasks import constants as TASK
from sqlalchemy.orm.exc import NoResultFound

class Task(db.Model):
	__tablename__ = "tasks"

	id = db.Column(db.Integer, db.Sequence('tasks_id_seq'), primary_key=True)
	title = db.Column(db.String(255), nullable=False)
	desc = db.Column(db.String(1023))
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	sub_tasks = db.relationship('SubTask', backref='tasks', lazy='dynamic')
	status = db.Column(db.Integer, default = TASK.TASK_STATUS_NONE)
	created_on = db.Column(db.DateTime, default = db.func.now())
	updated_on = db.Column(db.DateTime, default = db.func.now(), onupdate = db.func.now())
	deleted = db.Column(db.Boolean, default = False)
	def __init__(self, title, desc, user_id):
		self.title = title
		self.desc = desc
		self.user_id = user_id

class SubTask(db.Model):
	__tablename__ = "sub_tasks"
	id = db.Column(db.Integer, db.Sequence('sub_tasks_id_seq'), primary_key=True)
	title = db.Column(db.String(255), nullable=False)
	status = db.Column(db.Integer, default = TASK.TASK_STATUS_NONE)
	task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'))
	created_on = db.Column(db.DateTime, default = db.func.now())
	updated_on = db.Column(db.DateTime, default = db.func.now(), onupdate = db.func.now())
	deleted = db.Column(db.Boolean, default = False)

	def __init__(self, title, task_id):
		self.title = title
		self.user_id = user_id
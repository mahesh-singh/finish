from app import db
from app.users import constants as USER

class User(db.Model):
	__tablename__ = 'users'

	id = db.Column(db.Integer, db.Sequence('user_id_seq'), primary_key=True)
	f_name = db.Column(db.String(100))
	l_name = db.Column(db.String(100))
	full_name = db.Column(db.String(200))
	email = db.Column(db.String(200), unique = True)
	profile_url = db.Column(db.String(1000))
	created_on = db.Column(db.DateTime, default = db.func.now())
	updated_on = db.Column(db.DateTime, default = db.func.now(), onupdate = db.func.now())

	def __init__(self, f_name, l_name, name, email, profile_url):
		self.f_name = f_name
		self.l_name = l_name
		self.name = name
		self.email = email
		self.profile_url = profile_url
	
	def __repr__(self):
		return "<User(%d, %s, %s)>" % (self.id, self.full_name, self.email)


	

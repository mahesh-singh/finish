from app import db

class User(db.Model):
	__tablename__ = 'users'

	id = db.Coulmn(db.Integer, primary_key=True)
	

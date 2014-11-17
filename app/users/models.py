from app import db
from app.users import constants as USER
from app import login_manager
from sqlalchemy.orm.exc import NoResultFound


class User(db.Model):
	__tablename__ = 'users'

	id = db.Column(db.Integer, db.Sequence('users_id_seq'), primary_key=True)
	f_name = db.Column(db.String(100))
	l_name = db.Column(db.String(100))
	full_name = db.Column(db.String(200))
	email = db.Column(db.String(200), unique = True, nullable=False)
	profile_url = db.Column(db.String(1000))
	profile_pic = db.Column(db.String(1000))
	verified_email = db.Column(db.Boolean)
	created_on = db.Column(db.DateTime, default = db.func.now())
	updated_on = db.Column(db.DateTime, default = db.func.now(), onupdate = db.func.now())

	def __init__(self, f_name, l_name, full_name, email, profile_url, profile_pic, verified_email):
		self.f_name = f_name
		self.l_name = l_name
		self.full_name = full_name
		self.email = email
		self.profile_url = profile_url
		self.profile_pic = profile_pic
		self.verified_email = verified_email
	
	
	def get_id(self):
		try:
			return unicode(self.id)
		except Exception, e:
			raise NotImplementationError('No id attribiute')


	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	@login_manager.user_loader
	def load_user(user_id):
		return User.query.get(int(user_id))

	@classmethod
	def get_or_create(cls, data):
		"""
        data contains:
            {u'family_name': u'Surname',
            u'name': u'Name Surname',
            u'picture': u'https://link.to.photo',
            u'locale': u'en',
            u'gender': u'male',
            u'email': u'propper@email.com',
            u'birthday': u'0000-08-17',	
            u'link': u'https://plus.google.com/id',
            u'given_name': u'Name',
            u'id': u'Google ID',
            u'verified_email': True}
		"""
		try:

			user = cls.query.filter_by(email = data['email']).one()
			#Update user
			user.f_name = data['given_name']
			user.l_name = data['family_name']
			user.full_name = data['name'],
			user.profile_url = data['link'],
			user.profile_pic = data['picture'],
			user.verified_email = data['verified_email']  
			db.session.commit()
			return user
		except NoResultFound:
			user = cls(f_name = data['given_name'],
				l_name = data['family_name'],
				full_name = data['name'],
				email = data['email'],
				profile_url = data['link'],
				profile_pic = data['picture'],
				verified_email = data['verified_email'])
			db.session.add(user)
			db.session.commit()
			return user

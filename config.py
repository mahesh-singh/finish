class Config(object):
	DEBUG = False
	TESTING = False
	SQLALCHEMY_DATABASE_URI = ''
	CSRF_ENABLED = True
	CSRF_SESSION_KEY = "FinishingIsaKey"
	SECRET_KEY = 'finishingIsNotaSecretKey'
	GOOGLE_API_CLIENT_ID = '459708552145-afa0lh4entqtu0eohee36nv753q6b71u.apps.googleusercontent.com'
	GOOGLE_API_CLIENT_SECRET = 'NzbeIKinPLk1T-fFzlI_OOej'
	GOOGLE_API_SCOPE = 'https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email'
	GOOGLE_OAUTH2_URL = 'https://accounts.google.com/o/oauth2/'
	GOOGLE_API_URL = 'https://www.googleapis.com/oauth2/v1/'

class ProdConfig(Config):
	SQLALCHEMY_DATABASE_URI = ''	

class DevConfig(Config):
	SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123456@localhost/finish'

class QAConfig(Config):
	SQLALCHEMY_DATABASE_URI = ''		

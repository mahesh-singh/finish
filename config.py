class Config(object):
	DEBUG = False
	TESTING = False
	SQLALCHEMY_DATABASE_URI = ''
	CSRF_ENABLED = True
	CSRF_SESSION_KEY = "FinishingIsaKey"
	SECRET_KEY = 'finishingIsNotaSecretKey'

class ProdConfig(Config):
	SQLALCHEMY_DATABASE_URI = ''	

class DevConfig(Config):
	SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123456@localhost/finish'

class QAConfig(Config):
	SQLALCHEMY_DATABASE_URI = ''		

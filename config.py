import os
class Config(object):
    DEBUG = False
    TESTING = False
    
    #BASE DIRECTORY
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))  
    
    # Enable protection agains *Cross-site Request Forgery (CSRF)*
    CSRF_ENABLED     = True

    # Use a secure, unique and absolutely secret key for
    # signing the data. 
    CSRF_SESSION_KEY = "secret"

    # Secret key for signing cookies
    SECRET_KEY = "secret"

class ProductionConfig(Config):
    DATABASE_DRIVER = 'redis'

class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_DRIVER = 'redis'

class TestingConfig(Config):
    TESTING = True
    DATABASE_DRIVER = 'memory'

logging_config = {
		'version': 1,
		'loggers': {
			'': {  # root logger
				'level': 'DEBUG',
				'handlers': ['info_rotating_file_handler', 'error_file_handler'],
			},
		},
		'handlers': {
			'info_rotating_file_handler': {
				'level': 'DEBUG',
				'formatter': 'info',
				'class': 'logging.handlers.RotatingFileHandler',
				'filename': 'app.log',
				'mode': 'a',
				'maxBytes': 1048576,
				'backupCount': 10
			},
			'error_file_handler': {
				'level': 'WARNING',
				'formatter': 'error',
				'class': 'logging.FileHandler',
				'filename': 'error.log',
				'mode': 'a',
			},
		},
		'formatters': {
			'info': {
				'format': '%(asctime)s [%(levelname)s] [%(name)s::%(module)s|%(lineno)s::] %(message)s'
			},
			'error': {
				'format': '%(asctime)s [%(levelname)s] [%(name)s] [%(process)d::%(module)s|%(lineno)s::] %(message)s'
			},
		},
	}

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}

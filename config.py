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
    DATABASE_DRIVER = 'dict_cache'

class ProductionConfig(Config):
    DATABASE_DRIVER = 'redis_cache'

class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_DRIVER = 'dict_cache'

class TestingConfig(Config):
    TESTING = True


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}

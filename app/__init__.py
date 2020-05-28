from flask import Flask
from app.shortner.controllers import shortner_blueprint
from config import app_config
from celery import Celery


def create_app(config, name):
	application = Flask(__name__)
	#import the config based on the name dict
	application.config.from_object(app_config[config_name])
        #use dependancy injection to register the blueprints
        register_blueprints(application)
	#create_jobs
	create_celery(application, name)
	return application

def register_blueprints(application):
	application.register_blueprint(shortner_blueprint, url_prefix='/')
	
def create_celery(application, name):
        celery = Celery(name)
	celery.conf.update(application.config)
	return celerey


app = create_app('development', 'test-app')

if __name__ == "__main__":
    app.run()

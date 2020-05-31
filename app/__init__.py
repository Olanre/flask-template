__author__ = "Olanre Okunlola"

from flask import Flask

from app.main import main_blueprint
from config import app_config
#from celery import Celery

def register_blueprints(application):
	application.register_blueprint(main_blueprint, url_prefix='/')
	
def create_celery(application, name):
	mycelery = Celery(name)
	mycelery.conf.update(application.config)
	return mycelery

def create_app(config_name, name):
	application = Flask(__name__)
	#import the config based on the name dict
	application.config.from_object(app_config[config_name])
	#use dependancy injection to register the blueprints
	register_blueprints(application)
	#create_jobs
	#create_celery(application, name)
	return application




#app = create_app('development', 'development-app')

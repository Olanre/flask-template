__author__ = "Olanre Okunlola"

from flask import Flask

from app.main import main_blueprint
from config import app_config
from app.drivers.db import factory as db_factory
import os
from celery import Celery

def register_blueprints(application):
	application.register_blueprint(main_blueprint, url_prefix='/')
	
def create_celery(application, name):
	mycelery = Celery(name)
	mycelery.conf.update(application.config)
	return mycelery

def init_database(application):
	config = {"expiration_time" :100, 
			"host" : "localhost",
			"port":6379,
			"db" :0,  
			"prefix" : "",
			"partitions": 10, 
			"service_root" : os.getcwd()
	}
	db_instance = db_factory.create(application.config["DATABASE_DRIVER"], **config)
	if "DATABASE_DRIVER_OBJECT"  not in application.config:
		application.config['DATABASE_DRIVER_OBJECT'] = db_instance
	application.app_context().push()
	return db_instance


def create_app(config_name, name, db = None):
	application = Flask(__name__)
	#import the config based on the name dict
	application.config.from_object(app_config[config_name])
	#use dependancy injection to register the blueprints
	register_blueprints(application)
	if not db:
		init_database(application)
	else:
		application.config['DATABASE_DRIVER_OBJECT'] = db
	#create_jobs
	#create_celery(application, name)
	return application

"""
Some Testing

app = create_app('development', 'development-app')
db_instance1 = app.config['DATABASE_DRIVER_OBJECT']
db_instance2 = app.config['DATABASE_DRIVER_OBJECT']
print("Is db1 equal to db2 returns {}".format(db_instance1 == db_instance2 ))
db_instance1.put("hello","world")
print(db_instance1.get_all())
"""

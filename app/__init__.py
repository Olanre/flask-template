__author__ = "Olanre Okunlola"

from logger import log
from flask import Flask
from app.main import main_blueprint
from config import app_config, logging_config
from app.drivers.db import factory as db_factory
import os
from celery import Celery
from app.jobs.celery_tasks import *

def register_blueprints(application):
	application.register_blueprint(main_blueprint, url_prefix='/')
	
def create_celery_tasks(application):
	#schedule some tasks to be kicked off
	pass

def init_database(application):
	config = {"expiration_time" :100, 
			"host" : "localhost",
			"port":6379,
			"db" :0,  
			"prefix" : "",
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
	#create_celery_tasks(application, name)
	return application


from flask import Blueprint
from flask import current_app, g, redirect
from logger import log

def get_resource():
	log.info(f"The current app is {current_app} and the DB engine driver is {current_app.config['DATABASE_DRIVER_OBJECT']}")
	return "All Items", 200

def post_resource(new_resource):
	log.debug(f"Posting the new resource {new_resource}")
	return "Posted a new resource", 201

def get_resource_by_id(resource_id):
	log.debug(f"Getting the resource for {resource_id}")
	if resource_id:
		return "Here is the item " + resource_id, 200
	else:
		return "Unable to find the item " + resource_id, 404


def delete_resource(resource_id):
	log.debug(f"Deleting the resource for {resource_id}")
	if resource_id:
		return "Deleted the item " + resource_id, 202
	else:
		return "Unable to find the item " + resource_id, 404 

 

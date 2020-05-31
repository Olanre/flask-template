from flask import Blueprint

def get_resource():
	return "All Items", 200

def post_resource(new_resource):
	return "Posted a new resource", 201

def get_resource_by_id(resource_id):
	if resource_id:
		return "Here is the item " + resource_id, 200
	else:
		return "Unable to find the item " + resource_id, 404


def delete_resource(resource_id):
	if resource_id:
		return "Deleted the item " + resource_id, 202
	else:
		return "Unable to find the item " + resource_id, 404 

 

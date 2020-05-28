from flask import Blueprint


def get_urls():
	return "Shortner"

def shrink_url(long_url):
	return "Deleted item"

def get_url(tiny_url):
	return "Here is the item " + tiny_url


def delete_url(tiny_url):
	return "Deleted the item " + tiny_url

 

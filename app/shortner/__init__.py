from flask import Blueprint

from app.shortner.controllers import *

shortner_blueprint = Blueprint('shortner', __name__)
shortner_blueprint.add_url_rule('/url/', view_func=get_urls, methods=['GET'])
shortner_blueprint.add_url_rule('/url/<long_url>', view_func=shrink_url, methods=['POST'])
shortner_blueprint.add_url_rule('/url/<tiny_url>', view_func=get_url, methods=['GET'])
shortner_blueprint.add_url_rule('/url/<tiny_url>', view_func=delete_url, methods=['DELETE'])


from flask import Blueprint

from app.main.controllers import get_resource, post_resource, get_resource_by_id, delete_resource

main_blueprint = Blueprint('main', __name__)
main_blueprint.add_url_rule('/url/', view_func=get_resource, methods=['GET'])
main_blueprint.add_url_rule('/url/<new_resource>', view_func=post_resource, methods=['POST'])
main_blueprint.add_url_rule('/url/<resource_id>', view_func=get_resource_by_id, methods=['GET'])
main_blueprint.add_url_rule('/url/<resource_id>', view_func=delete_resource, methods=['DELETE'])


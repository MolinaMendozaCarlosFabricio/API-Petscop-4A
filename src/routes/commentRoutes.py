from flask import Blueprint, request
from src.controllers.commentController import create_comment_to_local, create_comment_to_post, create_comment_to_response, create_comment_to_service
from flask_jwt_extended import JWTManager

comment_blueprint = Blueprint('comments', __name__)

@comment_blueprint.route('/comment_post', methods=['POST'])
def create_comment_to_post_route():
    data = request.get_json()
    return create_comment_to_post(data)

@comment_blueprint.route('/comment_local', methods=['POST'])
def create_comment_to_local_route():
    data = request.get_json()
    return create_comment_to_local(data)

@comment_blueprint.route('/comment_service', methods=['POST'])
def create_comment_to_service_route():
    data = request.get_json()
    return create_comment_to_service(data)

@comment_blueprint.route('/response_comment', methods=['POST'])
def create_comment_to_response_route():
    data = request.get_json()
    return create_comment_to_response(data)
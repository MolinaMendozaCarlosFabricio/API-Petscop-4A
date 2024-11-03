from flask import Blueprint, request
from src.controllers.commentController import create_comment_to_local, create_comment_to_post, create_comment_to_response, create_comment_to_service, get_comments_of_post, get_comments_of_local, get_comments_of_service, get_comments_of_comment, edit_comment, add_reaction, remove_reaction, remove_comment_of_post, remove_comment_of_local, remove_comment_of_service, remove_response_of_comment
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

@comment_blueprint.route('/get_comments_of_post/<int:id_post>', methods=['GET'])
def get_comments_of_post_route(id_post):
    return get_comments_of_post(id_post)

@comment_blueprint.route('/get_comments_of_local/<int:id_local>', methods=['GET'])
def get_comments_of_local_route(id_local):
    return get_comments_of_local(id_local)

@comment_blueprint.route('/get_comments_of_service/<int:id_service>', methods=['GET'])
def get_comments_of_service_route(id_service):
    return get_comments_of_service(id_service)

@comment_blueprint.route('/get_comments_of_comment/<int:id_comment>', methods=['GET'])
def get_comments_of_comment_route(id_comment):
    return get_comments_of_comment(id_comment)

@comment_blueprint.route('/edit_comment/<int:id_comment>', methods=['PUT'])
def edit_comment_route(id_comment):
    data = request.get_json()
    return edit_comment(data ,id_comment)

@comment_blueprint.route('/add_reaction_of_comment/<int:id_comment>', methods=['PUT'])
def add_reaction_route(id_comment):
    return add_reaction(id_comment)

@comment_blueprint.route('/remove_reaction_of_comment/<int:id_comment>', methods=['PUT'])
def remove_reaction_route(id_comment):
    return remove_reaction(id_comment)

@comment_blueprint.route('/remove_comment_from_post/<int:id_comment>', methods=['DELETE'])
def remove_comment_of_post_route(id_comment):
    return remove_comment_of_post(id_comment)

@comment_blueprint.route('/remove_comment_from_local/<int:id_comment>', methods=['DELETE'])
def remove_comment_of_local_route(id_comment):
    return remove_comment_of_local(id_comment)

@comment_blueprint.route('/remove_comment_from_service/<int:id_comment>', methods=['DELETE'])
def remove_comment_of_service_route(id_comment):
    return remove_comment_of_service(id_comment)

@comment_blueprint.route('/remove_response_from_comment/<int:id_comment>', methods=['DELETE'])
def remove_response_of_comment_route(id_comment):
    return remove_response_of_comment(id_comment)
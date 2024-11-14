from flask import Blueprint, request
from src.controllers.repostController import create_repost, show_reposts, show_repost_by_user, delete_repost
from flask_jwt_extended import JWTManager

repost_blueprint = Blueprint('reposts', __name__, url_prefix='/reposts')

@repost_blueprint.route('/create', methods=['POST'])
def create_repost_route():
    data = request.get_json()
    return create_repost(data)

@repost_blueprint.route('/get', methods=['GET'])
def show_repost_route():
    return show_reposts()

@repost_blueprint.route('/get_by_user', methods=['POST'])
def show_reposts_by_user_route():
    data = request.get_json()
    return show_repost_by_user(data)

@repost_blueprint.route('/delete/<int:id_repost>', methods=['DELETE'])
def delete_repost_route(id_repost):
    return delete_repost(id_repost)
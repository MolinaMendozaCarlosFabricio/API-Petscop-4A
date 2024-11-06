from flask import Blueprint, request
from src.controllers.userNormallyController import crear_usuario_normally, get_normally_user_by_id, search_normally_users, edit_profile, delete_profile
from flask_jwt_extended import JWTManager

user_normally_blueprint = Blueprint('usersNormally', __name__)

@user_normally_blueprint.route('/registerUser', methods=['POST'])
def crear_usuario_ruta():
    data = request.get_json()
    return crear_usuario_normally(data)

@user_normally_blueprint.route('/get_normal_user_by_id/<int:id_user>', methods=['GET'])
def get_normally_user_by_id_route (id_user):
    return get_normally_user_by_id(id_user)

@user_normally_blueprint.route('/search_normal_users', methods=['POST'])
def search_normally_users_route():
    data = request.get_json()
    return search_normally_users(data)

@user_normally_blueprint.route('/edit_normal_user/<int:id_user>', methods=['PUT'])
def edit_profile_route(id_user):
    data = request.get_json()
    return edit_profile(data, id_user)

@user_normally_blueprint.route('/delete_normal_user/<int:id_user>', methods=['DELETE'])
def delete_profive_route(id_user):
    return delete_profile(id_user)
from flask import Blueprint, request
from src.controllers.userController import crear_usuario, login_usuario, obtener_usuario, get_user_by_id, edit_password_user, upgrade_user, downgrade_user, eliminar_usuario
from flask_jwt_extended import JWTManager

usuario_blueprint = Blueprint('usuarios', __name__)

@usuario_blueprint.route('/registrer_user', methods=['POST'])
def crear_usuario_ruta():
    data = request.get_json()
    return crear_usuario(data)

@usuario_blueprint.route('/login', methods=['POST'])
def login_ruta():
    data = request.get_json()
    return login_usuario(data)

@usuario_blueprint.route('/get_your_profile', methods=['GET'])
def obtener_usuario_ruta():
    return obtener_usuario()

@usuario_blueprint.route('/get_one_user/<int:user_id>', methods=['GET'])
def get_user_by_id_route(user_id):
    return get_user_by_id(user_id)

@usuario_blueprint.route('/edit_password/<int:user_id>', methods=['PUT'])
def edit_password_user_ruta(user_id):
    data = request.get_json()
    return edit_password_user(user_id, data)

@usuario_blueprint.route('/upgrade_user/<int:user_id>', methods=['PUT'])
def upgrade_user_ruta(user_id):
    return upgrade_user(user_id)

@usuario_blueprint.route('/downgrade_user/<int:user_id>', methods=['PUT'])
def downgrade_user_ruta(user_id):
    return downgrade_user(user_id)

@usuario_blueprint.route('/delete_user/<int:user_id>', methods=['DELETE'])
def eliminar_usuario_ruta(user_id):
    return eliminar_usuario(user_id)


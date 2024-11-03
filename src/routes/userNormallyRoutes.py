from flask import Blueprint, request
from src.controllers.userNormallyController import crear_usuario_normally
from flask_jwt_extended import JWTManager

user_normally_blueprint = Blueprint('usersNormally', __name__)

@user_normally_blueprint.route('/registerUser', methods=['POST'])
def crear_usuario_ruta():
    data = request.get_json()
    return crear_usuario_normally(data)
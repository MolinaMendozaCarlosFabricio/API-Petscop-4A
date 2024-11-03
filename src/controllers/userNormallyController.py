from flask import jsonify
from src.models.user import User, db
from src.models.user_normally import UserNormally

def crear_usuario_normally(data):
    # Obtener datos requeridos para `User`
    type_user = data.get('type_user')
    email = data.get('email')
    password = data.get('password')
    
    # Obtener datos específicos para `UserNormally`
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    birthdate = data.get('birthdate')
    profile_picture = data.get('profile_picture')

    # Verificar que todos los campos obligatorios estén presentes
    if not all([type_user, email, password, first_name, last_name, birthdate, profile_picture]):
        return jsonify({"mensaje": "Faltan campos obligatorios"}), 400

    # Comprobar si el correo electrónico ya existe
    if User.query.filter_by(email=email).first():
        return jsonify({"mensaje": "El email ya está registrado"}), 400

    # Crear el usuario en la tabla `Users`
    nuevo_usuario = User(type_user=type_user, email=email, password=password)
    db.session.add(nuevo_usuario)
    db.session.flush()  # Guardar provisionalmente para obtener `id_user` sin hacer commit

    # Crear el perfil específico en `UserNormally`, enlazado al nuevo usuario
    nuevo_usuario_normally = UserNormally(
        id_user=nuevo_usuario.id_user,
        first_name=first_name,
        last_name=last_name,
        birthdate=birthdate,
        profile_picture=profile_picture
    )
    db.session.add(nuevo_usuario_normally)
    db.session.commit()  # Confirmar ambos registros

    return jsonify({
        "mensaje": "Usuario normalmente creado",
        "id_user": nuevo_usuario.id_user,
        "type_user": nuevo_usuario.type_user,
        "email": nuevo_usuario.email,
        "first_name": nuevo_usuario_normally.first_name,
        "last_name": nuevo_usuario_normally.last_name
    }), 201

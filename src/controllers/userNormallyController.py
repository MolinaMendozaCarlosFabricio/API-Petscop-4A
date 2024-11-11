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
    if User.query.filter_by(email_user=email).first():
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
        "email": nuevo_usuario.email_user,
        "first_name": nuevo_usuario_normally.first_name,
        "last_name": nuevo_usuario_normally.last_name
    }), 201

def get_normally_user_by_id(id_user):
    result = (
        db.session.query(UserNormally, User)
        .join(User, UserNormally.id_user == User.id_user)
        .filter(UserNormally.id_user_normally == id_user)
        .first()
    )
    
    if not result:
        return jsonify({"Message": "Usuario normal no encontrado"}), 404
    
    user_normally, user = result

    return jsonify({
        "Message": "Usuario encontrado",
        "id_user": user.id_user,
        "email_user": user.email_user,
        "password_user": user.password_user,
        "type_user": user.type_user,
        "id_user_normally": user_normally.id_user_normally,
        "first_name": user_normally.first_name,
        "last_name": user_normally.last_name,
        "email": user.email_user,
        "birthdate": user_normally.birthdate.strftime('%Y-%m-%d'),
        "photo_profile": user_normally.profile_picture
    }), 200

def search_normally_users(data):
    query = (
        db.session.query(UserNormally, User)
        .join(User, UserNormally.id_user == User.id_user)
    )

    name = data.get('name')
    lastname = data.get('lastname')
    email = data.get('email')

    if name:
        query = query.filter(UserNormally.first_name.ilike(f"%{name}%"))
    
    if lastname:
        query = query.filter(UserNormally.last_name.ilike(f"%{lastname}%"))
    
    if email:
        query = query.filter(User.email_user.ilike(f"%{email}%"))

    results = query.all()

    if not results:
        return jsonify({"Message": "No se encontraron usuarios normales"}), 404

    normal_users_json = [{
        "id": user.id_user,
        "id_normally": user_normally.id_user_normally,
        "name": user_normally.first_name,
        "last_name": user_normally.last_name,
        "email": user.email_user,
        "birth_day": user_normally.birthdate,
        "photo_profile": user_normally.profile_picture
    } for user_normally, user in results]

    return jsonify(normal_users_json), 200

def edit_profile(data, id_user):
    editThisProfile = UserNormally.query.get(id_user)

    if not editThisProfile:
        return jsonify({"Message":"Perfil no encontrado"}), 404
    
    name = data.get('first_name')
    lastname = data.get('last_name')
    photo = data.get('profile_picture')

    if name:
        editThisProfile.first_name = name
    
    if lastname:
        editThisProfile.last_name = lastname
    
    if photo:
        editThisProfile.profile_picture = photo
    
    db.session.commit()

    return jsonify({
        "Message":"Usuario normal editado",
        "id" : editThisProfile.id_user_normally,
        "name" : editThisProfile.first_name,
        "lastname" : editThisProfile.last_name
    }), 200

def delete_profile(id_user):
    deleteThisNormalUser = UserNormally.query.get(id_user)

    if not deleteThisNormalUser:
        return jsonify({"Message":"No se encontró el usuario"}), 404

    deleteThisUser = User.query.filter(User.id_user == deleteThisNormalUser.id_user).all()

    if not deleteThisUser:
        return jsonify({"Message":"Usuario no encontrado, qué raro"}), 404
    
    db.session.delete(deleteThisNormalUser)
    
    for user in deleteThisUser:
        db.session.delete(user)
    
    db.session.commit()

    return jsonify({"Message": "Usuario normal eliminado"}), 200

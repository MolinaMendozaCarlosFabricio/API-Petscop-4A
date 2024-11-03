from flask import jsonify
from src.models.user import User, db
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

def crear_usuario(data):
    name = data.get('name')
    lastname = data.get('lastname')
    birthday = data.get('birthday')
    email = data.get('email')
    password = data.get('password')
    type_user = data.get('type_user')

    if not name or not email or not password or not lastname or not birthday or not type_user:
        return jsonify({"mensaje": "Faltan campos obligatorios"}), 400

    if User.query.filter_by(email_user=email).first():
        return jsonify({"mensaje": "El email ya está registrado"}), 400

    nuevo_usuario = User(name=name, lastname=lastname, birthday=birthday, email=email, password=password, type_user=type_user)
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({
        "mensaje": "Usuario creado con bcrypt",
        "id": nuevo_usuario.id_user,
        "nombre": nuevo_usuario.name_user,
        "apellido": nuevo_usuario.lastname_user,
        "email": nuevo_usuario.email_user
    }), 201

def login_usuario(data):
    email = data.get('email')
    password = data.get('password')
    user = User.query.filter_by(email_user=email).first()
    if not user:
        return jsonify({"mensaje": "Credenciales inválidas"}), 401
    if not user.check_password(password):
        return jsonify({"mensaje": "Credenciales inválidas"}), 401
    access_token = create_access_token(identity=user.id_user)
    return jsonify({"mensaje": "Inicio de sesión exitoso", "token": access_token}), 200

@jwt_required()
def obtener_usuario():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404
    return jsonify({
        "id": user.id_user,
        "nombre": user.name_user,
        "email": user.email_user
    }), 200

#@jwt_required()
def get_user_by_id(user_id):
    showThisUser = User.query.get(user_id)

    if not showThisUser:
        return jsonify({"Message" : "No se encontró al usuario"}), 404
    
    return jsonify({
        "id": showThisUser.id_user,
        "nombre": showThisUser.name_user,
        "apellido": showThisUser.lastname_user,
        "fecha_nacimiento": showThisUser.birthday_user,
        "email": showThisUser.email_user,
        "tipo_usuario": showThisUser.type_user.value 
    }), 200

#@jwt_required()
def search_users(data):
    query = User.query

    name = data.get('name')
    lastname = data.get('lastname')
    email = data.get('email')

    if name:
        query = query.filter(User.name_user.ilike(f"%{name}%"))
    
    if lastname:
        query = query.filter(User.lastname_user.ilike(f"%{lastname}%"))
    
    if email:
        query = query.filter(User.email_user.ilike(f"%{email}%"))
    
    users = query.all()

    users_json = [{
        "id": user.id_user,
        "nombre": user.name_user,
        "apellido": user.lastname_user,
        "fecha_nacimiento": user.birthday_user,
        "email": user.email_user,
        "tipo_usuario": user.type_user.value
    } for user in users]

    return jsonify(users_json), 200

#@jwt_required()
def edit_username(user_id, data):
    editThisUser = User.query.get(user_id)

    if not editThisUser:
        return jsonify({"Message": "Usuario no encontrado"}), 404
    
    name = data.get('name')
    lastname = data.get('lastname')

    if not name or not lastname:
        return jsonify({"Message": "Hay campos sin llenar"}), 404
    
    editThisUser.name_user = name
    editThisUser.lastname_user = lastname

    db.session.commit()

    return jsonify({
        "Message" : "Username actualizado",
        "id" : editThisUser.id_user,
        "name" : editThisUser.name_user,
        "lastname" : editThisUser.lastname_user
    }), 200

#@jwt_required()
def edit_password_user(user_id, data):
    editThisUser = User.query.get(user_id)

    if not editThisUser:
        return jsonify({"Message" : "Usuario no encontrado"}), 404
    
    new_password = data.get('password')

    if not new_password:
        return jsonify({"Message": "Ingrese la contraseña"}), 404
    
    editThisUser.password_user = bcrypt.generate_password_hash(data['password']).decode('utf-8')

    db.session.commit()

    return jsonify({
        "Message" : "Contraseña actualizada"
    }), 200

#@jwt_required()
def upgrade_user(user_id):
    upgradeThisUser = User.query.get(user_id)

    if not upgradeThisUser:
        return jsonify({"Message": "Usuario no encontrado"}), 404
    
    upgradeThisUser.type_user = "Suscriptor"

    db.session.commit()

    return jsonify({
        "Message": "Usuario actualizado a suscriptor",
        "id" : upgradeThisUser.id_user,
        "name" : upgradeThisUser.name_user,
        "lastname" : upgradeThisUser.lastname_user,
        "type_user" : upgradeThisUser.type_user.value,
    }), 200

#@jwt_required()
def downgrade_user(user_id):
    downgradeThisUser = User.query.get(user_id)

    if not downgradeThisUser:
        return jsonify({"Message": "Usuario no encontrado"}), 404
    
    downgradeThisUser.type_user = "Normal"

    db.session.commit()

    return jsonify({
        "Message": "Usuario rebajado a normal",
        "id" : downgradeThisUser.id_user,
        "name" : downgradeThisUser.name_user,
        "lastname" : downgradeThisUser.lastname_user,
        "type_user" : downgradeThisUser.type_user.value,
    }), 200

@jwt_required()
def eliminar_usuario(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({"mensaje": "Usuario eliminado"}), 200
from flask import jsonify
from src.models import db
from src.models.repost import  Repost
from src.models.user import User
from flask_jwt_extended import jwt_required, get_jwt_identity

#@jwt_required()
def create_repost(data):
    id_user = data.get('id_user')
    id_post = data.get('id_post')

    if not id_user or not id_post:
        return jsonify({"Message": "Hay campos sin llenar"}), 404
    
    new_repost = Repost(id_user=id_user, id_post=id_post)

    db.session.add(new_repost)
    db.session.commit()

    return jsonify({
        "Message": "Post compartido"    
    }), 200

#@jwt_required()
def show_reposts():
    results = db.session.query(User, Repost).join(Repost, User.id_user == Repost.id_user_repost).all()

    usersWhitRepost = []

    for user, repost in results:
        usersWhitRepost.append({
            "user_id": user.id_user,
            "name": user.name_user,
            "lastname": user.lastname_user,
            "post_id": repost.id_post_repost
        })

    return jsonify(usersWhitRepost), 200

#@jwt_required()
def show_repost_by_user(data):
    id_user = data.get('id_user')

    if not id_user:
        return jsonify({"Message" : "No se llenaron los campos"})
    
    results = (
        db.session.query(User, Repost)
        .join(Repost, User.id_user == Repost.id_user_repost)
        .filter(User.id_user == id_user)
        .all()
    )
    
    users_with_reposts = []

    for user, repost in results:
        users_with_reposts.append({
            "user_id": user.id_user,
            "name": user.name_user,
            "lastname": user.lastname_user,
            "post_id": repost.id_post_repost
        })

    return jsonify(users_with_reposts), 200

#@jwt_required
def delete_repost(data):

    id_user = data.get('id_user')
    id_post = data.get('id_post')

    if not id_user or not id_post:
        return jsonify({"Message": "Campos faltantes"}), 404

    repost = (
        db.session.query(Repost)
        .filter(Repost.id_user_repost == id_user)
        .filter(Repost.id_post_repost == id_post)
        .all()
        #Repost.query.get(id_repost)
    )

    if not repost:
        return jsonify({"Message" : "Repost no encontrado"}), 404
    
    db.session.delete(repost)
    db.session.commit()

    return jsonify({"Message" : "Repost eliminado"}), 200
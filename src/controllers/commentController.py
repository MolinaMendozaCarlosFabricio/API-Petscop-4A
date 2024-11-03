from flask import jsonify
from src.models import db
from src.models.comment import  Comment
from src.models.commentPost import Response_post
from src.models.commentLocal import Response_local
from src.models.commentService import Response_service
from src.models.responseComment import Response_comment
from flask_jwt_extended import jwt_required, get_jwt_identity

#@jwt_required()
def create_comment_to_post(data):
    body = data.get('body')
    id_user = data.get('id_user')
    id_post = data.get('id_post')

    if not body or not id_user or not id_post:
        return jsonify({"Message": "Campos faltantes"}), 404
    
    new_comment = Comment(body, id_user)
    new_response = Response_post(id_post=id_post, id_comment=new_comment.id_comment)

    db.session.add(new_comment)
    db.session.add(new_response)
    db.session.commit()

    return jsonify({
        "Message":"Comentario añadido a post"
    }), 200

#@jwt_required()
def create_comment_to_local(data):
    body = data.get('body')
    id_user = data.get('id_user')
    id_local = data.get('id_local')

    if not body or not id_user or not id_local:
        return jsonify({"Message": "Campos faltantes"}), 404
    
    new_comment = Comment(body, id_user)
    new_response = Response_local(id_local=id_local, id_comment=new_comment.id_comment)

    db.session.add(new_comment)
    db.session.add(new_response)
    db.session.commit()

    return jsonify({
        "Message":"Comentario añadido a local"
    }), 200

#@jwt_required()
def create_comment_to_service(data):
    body = data.get('body')
    id_user = data.get('id_user')
    id_service = data.get('id_service')

    if not body or not id_user or not id_service:
        return jsonify({"Message": "Campos faltantes"}), 404
    
    new_comment = Comment(body, id_user)
    new_response = Response_service(id_service=id_service, id_comment=new_comment.id_comment)

    db.session.add(new_comment)
    db.session.add(new_response)
    db.session.commit()

    return jsonify({
        "Message":"Comentario añadido a servicio"
    }), 200

#@jwt_required()
def create_comment_to_response(data):
    body = data.get('body')
    id_user = data.get('id_user')
    id_comment_to_response = data.get('id_comment')

    if not body or not id_user or not id_comment_to_response:
        return jsonify({"Message": "Campos faltantes"}), 404
    
    new_comment = Comment(body, id_user)

    db.session.add(new_comment)
    db.session.commit()

    new_response = Response_comment(id_comment=id_comment_to_response, id_response=new_comment.id_comment)

    db.session.add(new_response)
    db.session.commit()

    return jsonify({
        "Message":"Respuesta añadida a comentario"
    }), 200


from flask import jsonify
from src.models import db
from src.models.user import User
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
    
    db.session.add(new_comment)
    db.session.commit()

    new_response = Response_post(id_post, new_comment.id_comment)

    db.session.add(new_response)
    db.session.commit()

    return jsonify({
        "Message": "Comentario añadido a post"
    }), 200

#@jwt_required()
def create_comment_to_local(data):
    body = data.get('body')
    id_user = data.get('id_user')
    id_local = data.get('id_local')

    if not body or not id_user or not id_local:
        return jsonify({"Message": "Campos faltantes"}), 404
    
    new_comment = Comment(body, id_user)
    db.session.add(new_comment)
    db.session.commit()

    new_response = Response_local(id_local=id_local, id_comment=new_comment.id_comment)

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
    db.session.add(new_comment)
    db.session.commit()

    new_response = Response_service(id_service=id_service, id_comment=new_comment.id_comment)

    
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

def get_comments_of_post (id_post):
    comments = db.session.query(Comment, Response_post, User).join(Comment, Comment.id_comment == Response_post.id_response_to_post).join(User, Comment.id_user_comment == User.id_user).filter(Response_post.id_post_to_comment == id_post).all()

    comments_of_post = []

    for comment, response_post, user in comments:
        comments_of_post.append({
            "id_post": response_post.id_post_to_comment,
            "id_comment": comment.id_comment,
            "body": comment.body_comment,
            "reactions": comment.amount_reactions_comment,
            "user_id": user.id_user,
            "name_user": user.name_user,
            "lastname_user": user.lastname_user
        })

    return jsonify(comments_of_post), 200

def get_comments_of_local (id_local):
    comments = db.session.query(Comment, Response_local, User).join(Comment, Comment.id_comment == Response_local.id_response_to_local).join(User, Comment.id_user_comment == User.id_user).filter(Response_local.id_local_to_comment == id_local).all()

    comments_of_local = []

    for comment, response_local, user in comments:
        comments_of_local.append({
            "id_local": response_local.id_local_to_comment,
            "id_comment": comment.id_comment,
            "body": comment.body_comment,
            "reactions": comment.amount_reactions_comment,
            "user_id": user.id_user,
            "name_user": user.name_user,
            "lastname_user": user.lastname_user
        })

    return jsonify(comments_of_local), 200

def get_comments_of_service (id_service):
    comments = db.session.query(Comment, Response_service, User).join(Comment, Comment.id_comment == Response_service.id_response_to_service).join(User, Comment.id_user_comment == User.id_user).filter(Response_service.id_service_to_comment == id_service).all()

    comments_of_service = []

    for comment, response_service, user in comments:
        comments_of_service.append({
            "id_service": response_service.id_service_to_comment,
            "id_comment": comment.id_comment,
            "body": comment.body_comment,
            "reactions": comment.amount_reactions_comment,
            "user_id": user.id_user,
            "name_user": user.name_user,
            "lastname_user": user.lastname_user
        })

    return jsonify(comments_of_service), 200

def get_comments_of_comment(id_comment):
    comments = (
        db.session.query(Comment, Response_comment, User)
        .select_from(Response_comment)
        .join(Comment, Response_comment.id_comment_to_response == Comment.id_comment)
        .join(User, Comment.id_user_comment == User.id_user)
        .filter(Response_comment.id_comment_to_response == id_comment)
        .all()
    )

    comments_of_comment = []

    for comment, response_comment, user in comments:
        comments_of_comment.append({
            "id_comment": response_comment.id_comment_to_response,
            "id_response": comment.id_comment,
            "body": comment.body_comment,
            "reactions": comment.amount_reactions_comment,
            "user_id": user.id_user,
            "name_user": user.name_user,
            "lastname_user": user.lastname_user
        })

    return jsonify(comments_of_comment), 200

def edit_comment(data, id_comment):
    editThisComment = Comment.query.get(id_comment)

    if not editThisComment:
        return jsonify({"Message": "No se encontró el comentario"}), 404

    body = data.get('body')

    if not body:
        return jsonify({"Message":"Campos faltantes"}), 404
    
    editThisComment.body_comment = body

    db.session.commit()

    return jsonify({"Message": "Comentario editado"}), 200

def add_reaction(id_comment):
    editThisComment = Comment.query.get(id_comment)

    if not editThisComment:
        return jsonify({"Message": "No se encontró el comentario"}), 404
    
    editThisComment.amount_reactions_comment = editThisComment.amount_reactions_comment + 1

    db.session.commit()

    return jsonify({"Message": "Reacción añadida a comentario"}), 200

def remove_reaction(id_comment):
    editThisComment = Comment.query.get(id_comment)

    if not editThisComment:
        return jsonify({"Message": "No se encontró el comentario"}), 404
    
    editThisComment.amount_reactions_comment = editThisComment.amount_reactions_comment - 1

    db.session.commit()

    return jsonify({"Message": "Reacción quitada a comentario"}), 200

def remove_comment_of_post(id_comment):
    deleteThisComment = Comment.query.get(id_comment)
    deleteThisRelation = Response_post.query.filter(Response_post.id_response_to_post == id_comment).all()  # Obtiene todas las relaciones que coincidan

    if not deleteThisComment:
        return jsonify({"Message": "Este comentario ya no existe"}), 404
    
    if not deleteThisRelation:
        return jsonify({"Message": "No hay relaciones para eliminar"}), 404

    for relation in deleteThisRelation:
        db.session.delete(relation)

    db.session.delete(deleteThisComment)
    db.session.commit()

    return jsonify({"Message": "Comentario eliminado del post"}), 200

def remove_comment_of_local(id_comment):
    deleteThisComment = Comment.query.get(id_comment)
    deleteThisRelation = Response_local.query.filter(Response_local.id_response_to_local == id_comment).all()  # Obtiene todas las relaciones que coincidan

    if not deleteThisComment:
        return jsonify({"Message": "Este comentario ya no existe"}), 404
    
    if not deleteThisRelation:
        return jsonify({"Message": "No hay relaciones para eliminar"}), 404

    for relation in deleteThisRelation:
        db.session.delete(relation)

    db.session.delete(deleteThisComment)
    db.session.commit()

    return jsonify({"Message": "Comentario eliminado del local"}), 200

def remove_comment_of_service(id_comment):
    deleteThisComment = Comment.query.get(id_comment)
    deleteThisRelation = Response_service.query.filter(Response_service.id_response_to_service == id_comment).all()  # Obtiene todas las relaciones que coincidan

    if not deleteThisComment:
        return jsonify({"Message": "Este comentario ya no existe"}), 404
    
    if not deleteThisRelation:
        return jsonify({"Message": "No hay relaciones para eliminar"}), 404

    for relation in deleteThisRelation:
        db.session.delete(relation)

    db.session.delete(deleteThisComment)
    db.session.commit()

    return jsonify({"Message": "Comentario eliminado del servicio"}), 200

def remove_response_of_comment(id_comment):
    deleteThisComment = Comment.query.get(id_comment)
    deleteThisRelation = Response_comment.query.filter(Response_comment.id_response_to_comment == id_comment).all()  # Obtiene todas las relaciones que coincidan

    if not deleteThisComment:
        return jsonify({"Message": "Este comentario ya no existe"}), 404
    
    if not deleteThisRelation:
        return jsonify({"Message": "No hay relaciones para eliminar"}), 404

    for relation in deleteThisRelation:
        db.session.delete(relation)

    db.session.delete(deleteThisComment)
    db.session.commit()

    return jsonify({"Message": "Respuesta eliminada del comentario"}), 200


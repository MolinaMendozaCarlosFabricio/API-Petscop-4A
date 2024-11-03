from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from dotenv import load_dotenv
import os

from . import db
load_dotenv()  

class Comment (db.Model):
    schema_name = os.getenv('SCHEMA_NAME')
    __tablename__ = 'comments'
    __table_args__ = {'schema': schema_name }
    id_comment = db.Column(db.Integer, primary_key=True)
    body_comment = db.Column(db.Text, nullable=False)
    amount_reactions_comment = db.Column(db.Integer, nullable=False, default=0)
    id_user_comment = db.Column(db.Integer, ForeignKey(f'{schema_name}.users.id_user'))

    user = relationship('User', back_populates='comments', lazy='joined')
    response_to_post = relationship('Response_post', back_populates='comments', lazy='joined')
    response_to_local = relationship('Response_local', back_populates='comments', lazy='joined')
    response_to_service = relationship('Response_service', back_populates='comments', lazy='joined')
    response_to_comment = relationship('Response_post', foreign_keys=f'{schema_name}.response_to_comment.id_comment_to_response', back_populates='comentary_of_comment', lazy='joined')
    comment_to_response = relationship('Response_post', foreign_keys=f'{schema_name}.response_to_comment.id_response_to_comment', back_populates='response_of_comment', lazy='joined')

    def __init__(self, body, id_user):
        self.body_comment = body
        self.amount_reactions_comment = 0
        self.id_user_comment = id_user

from src.models.user import User
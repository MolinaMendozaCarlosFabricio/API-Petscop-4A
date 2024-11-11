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
    id_user_comment = db.Column(db.Integer, ForeignKey(f'{schema_name}.users.id_user'))

    user = relationship('User', back_populates='comments', lazy='joined')

    response_to_post = relationship('Response_post', back_populates='comment', lazy='joined')

    response_to_local = relationship('Response_local', back_populates='comment', lazy='joined')

    comentary = relationship('Response_comment', foreign_keys='Response_comment.id_comment_to_response', back_populates='comment', lazy='joined')
    response = relationship('Response_comment', foreign_keys='Response_comment.id_response_to_comment', back_populates='response', lazy='joined')


    def __init__(self, body, id_user):
        self.body_comment = body
        self.id_user_comment = id_user

from src.models.user import User
from src.models.commentPost import Response_post
from src.models.commentLocal import Response_local
from src.models.responseComment import Response_comment
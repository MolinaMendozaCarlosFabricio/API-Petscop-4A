from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from dotenv import load_dotenv
import os

from . import db
load_dotenv()

class Response_post(db.Model):
    schema_name = os.getenv('SCHEMA_NAME')
    __tablename__ = 'response_to_post'
    __table_args__ = {'schema': schema_name }
    id_response_post = db.Column(db.Integer, primary_key=True)
    id_post_to_comment = db.Column(db.String, nullable=False)
    id_response_to_post = db.Column(db.Integer, ForeignKey(f'{schema_name}.comments.id_comment'))

    comment = relationship('Comment', back_populates='response_to_post', lazy='joined')

    def __init__(self, id_post, id_comment):
        self.id_post_to_comment = id_post
        self.id_response_to_post = id_comment

from src.models.comment import Comment
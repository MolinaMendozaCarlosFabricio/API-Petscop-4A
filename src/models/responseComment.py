from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from dotenv import load_dotenv
import os

from . import db
load_dotenv()

class Response_comment(db.Model):
    schema_name = os.getenv('SCHEMA_NAME')
    __tablename__ = 'response_to_comment'
    __table_args__ = {'schema': schema_name }
    id_response_comment = db.Column(db.Integer, primary_key=True)
    id_comment_to_response = db.Column(db.Integer, ForeignKey(f'{schema_name}.comments.id_comment'))
    id_response_to_comment = db.Column(db.Integer, ForeignKey(f'{schema_name}.comments.id_comment'))

    # Relaciones con Comment, especificando foreign_keys
    comment = relationship('Comment', foreign_keys=[id_comment_to_response], back_populates='comentary')
    response = relationship('Comment', foreign_keys=[id_response_to_comment], back_populates='response')


    def __init__(self, id_comment, id_response):
        self.id_comment_to_response = id_response
        self.id_response_to_comment = id_comment

from src.models.comment import Comment
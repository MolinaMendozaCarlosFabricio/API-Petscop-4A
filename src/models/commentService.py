from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from dotenv import load_dotenv
import os

from . import db
load_dotenv()

class Response_service(db.Model):
    schema_name = os.getenv('SCHEMA_NAME')
    __tablename__ = 'response_to_service'
    __table_args__ = {'schema': schema_name }
    id_response_service = db.Column(db.Integer, primary_key=True)
    id_service_to_comment = db.Column(db.Integer, nullable=False)
    id_comment_to_service = db.Column(db.Integer, ForeignKey(f'{schema_name}.comments.id_comment'))

    comment = relationship('Comment', back_populates='response_to_service', lazy='joined')

    def __init__(self, id_service, id_comment):
        self.id_service_to_comment = id_service
        self.id_comment_to_service = id_comment

from src.models.comment import Comment
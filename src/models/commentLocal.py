from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from dotenv import load_dotenv
import os

from . import db
load_dotenv()

class Response_local(db.Model):
    schema_name = os.getenv('SCHEMA_NAME')
    __tablename__ = 'response_to_local'
    __table_args__ = {'schema': schema_name }
    id_response_local = db.Column(db.Integer, primary_key=True)
    id_local_to_comment = db.Column(db.String, nullable=False)
    id_response_to_local = db.Column(db.Integer, ForeignKey(f'{schema_name}.comments.id_comment'))

    comment = relationship('Comment', back_populates='response_to_local', lazy='joined')

    def __init__(self, id_local, id_comment):
        self.id_local_to_comment = id_local
        self.id_response_to_local = id_comment

from src.models.comment import Comment
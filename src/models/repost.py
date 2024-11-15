from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from dotenv import load_dotenv
import os

from . import db
load_dotenv()  

class Repost(db.Model):
    schema_name = os.getenv('SCHEMA_NAME')
    __tablename__ = 'reposts'
    __table_args__ = {'schema': schema_name }
    # id_repost = db.Column(db.Integer, primary_key=True)
    id_user_repost = db.Column(db.Integer, ForeignKey(f'{schema_name}.users.id_user'), primary_key=True)
    id_post_repost = db.Column(db.String, nullable=False, primary_key=True)

    user = relationship('User', back_populates='reposts', lazy='joined')

    def __init__(self, id_user, id_post):
        self.id_user_repost = id_user
        self.id_post_repost = id_post
    
    def __repr__(self):
        return f'<Repost {self.id_repost}>'

from src.models.user import User
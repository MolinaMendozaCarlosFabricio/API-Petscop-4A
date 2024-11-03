from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from dotenv import load_dotenv
import os

from src.models import db

load_dotenv() 

class UserNormally(db.Model):
    schema_name = os.getenv('SCHEMA_NAME')
    __tablename__ = 'usernormally'
    __table_args__ = {'schema': schema_name}

    id_user_normally = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, ForeignKey(f"{schema_name}.users.id_user"), nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(35), nullable=False)
    birthdate = db.Column(db.Date, nullable=False)
    profile_picture = db.Column(db.String(20), nullable=False)

    user = db.relationship("User", back_populates="user_normally")

    def __repr__(self):
        return f'<UserNormally {self.first_name} {self.last_name}>'

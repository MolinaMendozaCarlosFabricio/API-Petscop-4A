from flask_bcrypt import Bcrypt
from sqlalchemy.orm import relationship
from dotenv import load_dotenv
import os
from sqlalchemy import Enum
import enum

from . import db
bcrypt = Bcrypt()
load_dotenv()  

class TypeUserDateEnum(enum.Enum):
    Normal = "Normal"
    Local = "Local"
    Service = "Service"
    
class User(db.Model):    
    schema_name = os.getenv('SCHEMA_NAME')
    __tablename__ = 'users'
    __table_args__ = {'schema': schema_name}
    id_user = db.Column(db.Integer, primary_key=True)
    
    email_user = db.Column(db.String(255), nullable=False, unique=True)
    password_user = db.Column(db.String(255), nullable=False)
    type_user = type_user = db.Column(
        Enum('Normal', 'Local', 'Service', name='type_user_date', schema=schema_name),
        nullable=False
    )

    reposts = db.relationship('Repost', back_populates='user', lazy='joined')
    comments = db.relationship('Comment', back_populates='user', lazy='joined')
    user_normally = db.relationship("UserNormally", back_populates="user", uselist=False)

    def __init__(self, email, password, type_user):
        self.email_user = email
        self.password_user = bcrypt.generate_password_hash(password).decode('utf-8')
        self.type_user = type_user

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_user, password)

    def __repr__(self):
        return f'<User {self.email_user}>'

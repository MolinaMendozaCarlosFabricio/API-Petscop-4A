from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from sqlalchemy.dialects.postgresql import ENUM
from dotenv import load_dotenv
import os

from src.models import db

load_dotenv() 

bcrypt = Bcrypt()

class User(db.Model):
    schema_name = os.getenv('SCHEMA_NAME')
    __tablename__ = 'users'
    __table_args__ = {'schema': schema_name}

    id_user = db.Column(db.Integer, primary_key=True)
    type_user = db.Column(
        ENUM('UsuarioNormally', 'Local', 'Service', name='type_user_enum', schema=schema_name),
        nullable=False
    )
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)

    user_normally = db.relationship("UserNormally", back_populates="user", uselist=False)

    def __init__(self, type_user, email, password):
        self.type_user = type_user
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User {self.email}>'

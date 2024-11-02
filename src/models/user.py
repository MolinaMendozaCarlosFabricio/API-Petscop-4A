from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
import os
from sqlalchemy import Enum
import enum

db = SQLAlchemy()
bcrypt = Bcrypt()
load_dotenv()  

class TypeUserDateEnum(enum.Enum):
    Normal = "Normal"
    Suscriptor = "Suscriptor"
    Admin = "Admin"
    
class User(db.Model):    
    schema_name = os.getenv('SCHEMA_NAME')
    __tablename__ = 'users'
    __table_args__ = {'schema': schema_name}
    id_user = db.Column(db.Integer, primary_key=True)
    name_user = db.Column(db.String(100), nullable=False)
    lastname_user = db.Column(db.String(100), nullable= False)
    birthday_user = db.Column(db.Date, nullable=False)
    email_user = db.Column(db.String(255), nullable=False, unique=True)
    password_user = db.Column(db.String(255), nullable=False)
    type_user = db.Column(Enum(TypeUserDateEnum), nullable=False)

    def __init__(self, name, lastname, birthday, email, password, type_user):
        self.name_user = name
        self.lastname_user = lastname
        self.birthday_user = birthday
        self.email_user = email
        self.password_user = bcrypt.generate_password_hash(password).decode('utf-8')
        self.type_user = type_user

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_user, password)

    def __repr__(self):
        return f'<User {self.nombre}>'

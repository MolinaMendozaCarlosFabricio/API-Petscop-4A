from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# Instancia de SQLAlchemy
db = SQLAlchemy()

# Importar los modelos para asegurarse de que están registrados en SQLAlchemy
from .user import User
from .user_normally import UserNormally

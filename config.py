import os
from dotenv import load_dotenv
from google.oauth2 import service_account
from googleapiclient.discovery import build

load_dotenv()  

# Datos del bucket de google drive
SCOPES = ['https://www.googleapis.com/auth/drive.file']
SERVICE_ACCOUNT_FILE = os.getenv('GOOGLE_CREDENTIALS_PATH')
credentials = service_account.Credentials.from_service_account_file(
SERVICE_ACCOUNT_FILE, scopes=SCOPES)
drive_service = build('drive', 'v3', credentials=credentials)

class Config:
    # Carga la URI de la base de datos y la clave secreta para JWT desde las variables de entorno
    #DATABASE_URL = postgresql://user:password@localhost/database
    #JWT_SECRET_KEY = 'PALABRA_SECRETAÑ'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

config = {
    'development': Config,
    'testing': Config
}

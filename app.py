from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import config
from src.routes.userNormallyRoutes import user_normally_blueprint
from src.models.user_normally import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(config['development'])
    db.init_app(app)
    jwt = JWTManager(app)
    app.register_blueprint(user_normally_blueprint)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
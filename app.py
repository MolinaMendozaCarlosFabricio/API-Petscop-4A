from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import config
from src.routes.userRoutes import usuario_blueprint
from src.routes.repostRoutes import repost_blueprint
# from src.routes.commentRoutes import comment_blueprint
from src.routes.userNormallyRoutes import user_normally_blueprint
from src.routes.driveRoutes import drive_bp
from src.models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(config['development'])
    db.init_app(app)
    jwt = JWTManager(app)
    app.register_blueprint(usuario_blueprint)
    app.register_blueprint(repost_blueprint)
    # app.register_blueprint(comment_blueprint)
    app.register_blueprint(user_normally_blueprint)
    app.register_blueprint(drive_bp)
    return app

if __name__ == '__main__':
    app = create_app()
    CORS(app)
    app.run(debug=True)

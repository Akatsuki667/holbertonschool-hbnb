from config import DevelopmentConfig
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

jwt = JWTManager()

bcrypt = Bcrypt()

db = SQLAlchemy()


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Makes bcrypt hashing available through app object
    bcrypt.init_app(app)

    # initialize jwt auth handling through app object
    jwt.init_app(app)

    # Initialize database
    db.init_app(app)
    with app.app_context():
        db.create_all()
    # Register v1 Blueprint (which registers api namespaces)
    from app.api.v1 import api_v1
    app.register_blueprint(api_v1)

    return app
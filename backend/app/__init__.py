from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config import Config
import logging

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    CORS(app)  # Enable Cross-Origin Resource Sharing

    with app.app_context():
        try:
            db.create_all()
            logging.info("✅ Database tables created successfully.")
        except Exception as e:
            logging.error(f"❌ Database initialization failed: {e}")

    # Import routes and register blueprint
    from .routes import routes
    app.register_blueprint(routes, url_prefix="/api")
    
    logging.info("✅ API Routes registered at /api/*")

    return app

from flask import Flask, render_template
from dotenv import load_dotenv
from app.utils import sync_words
import os
from app.main import main
from app.practice import quiz
from app.auth import auth
from app.user import user
from app.db import db
from app.extensions import bcrypt, csrf, login_manager  # Add login_manager to imports
from flask_login import LoginManager

def register_blueprints(app):
    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(user)
    app.register_blueprint(quiz)

def register_error_handlers(app):
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return render_template('errors/500.html'), 500

def create_app():
    load_dotenv()

    app = Flask(__name__)
    
    # Configuration
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    csrf.init_app(app)
    login_manager.init_app(app)
    
    # Configure Flask-Login
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Please log in to access this page.'
    login_manager.login_message_category = 'info'

    with app.app_context():
        register_blueprints(app)
        register_error_handlers(app)
        
        db.create_all()
        sync_words.sync_words_from_csv('data/words.csv')
        
    return app
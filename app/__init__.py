from flask import Flask
from dotenv import load_dotenv
from app.utils import sync_words
import os
from app.main import main
from app.quiz import quiz
from app.auth import auth
from app.user import user
from app.db import db
from app.extensions import bcrypt, csrf


def register_blueprints(app):
    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(user)
    app.register_blueprint(quiz)

def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    bcrypt.init_app(app)
    csrf.init_app(app)

    with app.app_context():
        register_blueprints(app)

        
        db.create_all()
        sync_words.sync_words_from_csv('data/words.csv')
        
    return app
    
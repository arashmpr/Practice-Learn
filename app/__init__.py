from flask import Flask, render_template
from dotenv import load_dotenv

from app.config import Config
from app.db import db, init_db
from app.extensions import bcrypt, csrf, login_manager

def register_blueprints(app):
    from app.blueprints.auth import auth
    from app.blueprints.main import main
    from app.blueprints.practice import practice
    from app.blueprints.user import user

    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(user)
    app.register_blueprint(practice)

def register_error_handlers(app):
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return render_template('errors/500.html'), 500

def init_extensions(app):
    db.init_app(app)
    bcrypt.init_app(app)
    csrf.init_app(app)
    login_manager.init_app(app)

def configure_login():
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Please log in to access this page.'
    login_manager.login_message_category = 'info'

def create_app(initialize_db=True):

    load_dotenv()

    app = Flask(__name__)
    app.config.from_object(Config)

    init_extensions(app)
    configure_login()    

    with app.app_context():
        register_blueprints(app)
        register_error_handlers(app)
        
        if initialize_db:
            init_db()
        
    return app
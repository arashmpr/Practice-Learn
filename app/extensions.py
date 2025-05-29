from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

bcrypt = Bcrypt()
csrf = CSRFProtect()
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    from app.models import User  # Import here to avoid circular imports
    return User.query.get(int(user_id))
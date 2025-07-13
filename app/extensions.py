from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager

bcrypt = Bcrypt()
csrf = CSRFProtect()
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    from app.models.User import User
    return User.query.get(int(user_id))
from flask import Blueprint

auth = Blueprint(
    'auth',                          
    __name__,                    
    template_folder='../templates/auth'
)

from . import routes
from . import forms
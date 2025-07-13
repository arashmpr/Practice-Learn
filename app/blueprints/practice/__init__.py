from flask import Blueprint

practice = Blueprint(
    'practice',                          
    __name__,
    template_folder='../templates/practice'                     
)

from . import routes
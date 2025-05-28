from flask import Blueprint

quiz = Blueprint(
    'quiz',                          
    __name__,
    template_folder='../templates/quiz',
    static_folder='../static/quiz',
    static_url_path='/static/quiz'                        
)

from . import routes
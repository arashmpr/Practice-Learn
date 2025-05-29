from flask import Blueprint, render_template
from flask_login import current_user
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def index():
    current_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    quizzes = ['Article Quiz']
    return render_template('pages/home.html', 
                         current_time=current_time,
                         quizzes=quizzes)
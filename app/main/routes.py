from flask import Blueprint, render_template
from flask_login import current_user
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('pages/home.html')
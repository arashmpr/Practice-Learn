from flask import Blueprint, render_template
from flask_login import current_user
from datetime import datetime
from ..main import main

@main.route('/')
def home():
    return render_template('pages/home.html')
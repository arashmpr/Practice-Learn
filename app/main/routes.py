from flask import render_template
from ..main import main

@main.route('/')
def home():
    return render_template('pages/home.html')
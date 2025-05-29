from flask import render_template
from ..main import main

@main.route('/')
def home():
    quizzes = ['Article Quiz', 'PLural Quiz', 'Definition Quiz']
    return render_template('pages/home.html',
                           quizzes=quizzes)
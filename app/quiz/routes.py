from flask import render_template, request, redirect, url_for, session
from flask_login import current_user
from app.models.Word import Word
from app.quiz.strategies import QUIZ_STRATEGIES
import random
from ..quiz import quiz
from app.extensions import csrf
from . import utils


@quiz.route('/list')
def list():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.register'))
    lectures = utils.get_lectures()

    return render_template('quiz-list.html', quizzes=quizzes, lectures=lectures)

@quiz.route('/start/')
def start():
    # get request args
    quiz_type = request.args.get("quiz_type")
    num_questions = int(request.args.get("num_questions", 10))
    selected_lessons = request.args.getlist("lessons")
    has_definition = request.args.get("has_definition")
    has_plural = request.args.get("has_plural")
    has_article = request.args.get("has_article")
    has_time_limit = request.args.get("has_time_limit")
    time_limit = request.args.get("time_limit")

    settings_info = {
        "num_questions": num_questions,
        "selected_lectures": selected_lectures,
        "has_definition": has_definition,
        "has_plural": has_plural,
        "has_article": has_article,
        "has_time_limit": has_time_limit,
        "time_limit": time_limit
    }

    if quiz_type not in QUIZ_STRATEGIES:
        return "Invalid quiz type", 400
    
    if selected_lectures:
        lecture_ids = [int(lecture_id) for lecture_id in selected_lectures]
        words = Word.query.filter(Word.lektion.in_(lecture_ids)).all()
    else:
        words = Word.query.all()
    
    if len(words) == 0:
        return "No words found in that lecture", 400
    selected = random.sample(words, min(num_questions, len(words)))

    session['quiz_type'] = quiz_type
    session['quiz_words'] = [word.id for word in selected]
    session['current_idx'] = 0
    session['score'] = 0

    return redirect(url_for("quiz.show"))

@quiz.route('/quiz/')
def show():
    quiz_type = session['quiz_type']
    strategy = QUIZ_STRATEGIES.get(quiz_type)
    if not strategy:
        return "No quiz strategy set", 400
    
    current_idx = session.get('current_idx', 0)
    word_ids = session.get('quiz_words', [])
    if current_idx >= len(word_ids):
        return redirect(url_for('quiz.results'))
    
    word = Word.query.get(word_ids[current_idx])

    return strategy.render_question(word, current_idx + 1, len(word_ids))

@quiz.route('/submit/', methods=['POST'])
@csrf.exempt
def submit():
    quiz_type = session['quiz_type']
    strategy = QUIZ_STRATEGIES.get(quiz_type)
    current_idx = session.get('current_idx', 0)
    word_ids = session.get('quiz_words', [])
    word = Word.query.get(word_ids[current_idx])
    if strategy.check_answers(word, request):
        session['score'] += 1
    
    session["current_idx"] = current_idx + 1

    if current_idx + 1 >= len(word_ids):
        return redirect(url_for('quiz.results'))
    else:
        return redirect(url_for('quiz.show'))

@quiz.route('/results/')
def results():
    quiz_type = session['quiz_type']
    strategy = QUIZ_STRATEGIES.get(quiz_type)
    word_ids = session.get('quiz_words', [])
    score = session.get('score', 0)
    total = len(word_ids)

    return strategy.render_results(word_ids, score, total)
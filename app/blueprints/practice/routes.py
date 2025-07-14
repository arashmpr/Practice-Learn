from flask import render_template, request, redirect, url_for, session
from flask_login import current_user
from app.models.Word import Word
from ..practice import practice
from app.extensions import csrf
from app.services import PracticeService


@practice.route('/list')
def show_list():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.register'))
    
    practices = PracticeService.get_practices()
    print("Got the practices")
    lessons = PracticeService.get_lessons()
    print("Got the lessons")

    return render_template('practice/list.html', practices=practices, lessons=lessons)

@practice.route('/start/')
def start():

    practice_type = request.args.get("practice_type")
    selected_lessons = request.args.getlist("lessons")
    total_questions = request.args("num_questions")

    if practice_type not in PRACTICE_STRATEGIES:
        return "Invalid Practice Type", 400
    
    practice_strategy = PRACTICE_STRATEGIES.get(practice_type)
    practice_strategy.create()

    session['practice_type'] = quiz_type
    session['current_idx'] = 0
    session['score'] = 0

    return redirect(url_for("practice.show"))

@practice.route('/quiz/')
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

@practice.route('/submit/', methods=['POST'])
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

@practice.route('/results/')
def results():
    quiz_type = session['quiz_type']
    strategy = QUIZ_STRATEGIES.get(quiz_type)
    word_ids = session.get('quiz_words', [])
    score = session.get('score', 0)
    total = len(word_ids)

    return strategy.render_results(word_ids, score, total)
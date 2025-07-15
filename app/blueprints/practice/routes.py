from flask import render_template, request, redirect, url_for, session
from flask_login import current_user
from app.models.Word import Word
from ..practice import practice
from app.extensions import csrf
from app.services import PracticeService
from app.services.practice_service import PRACTICE_STRATEGIES
from app.repositories import PracticeSessionRepository


@practice.route('/list')
def show_list():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.register'))
    
    practices = PracticeService.get_practices()
    lessons = PracticeService.get_lessons()

    return render_template('practice/list.html', practices=practices, lessons=lessons)

@practice.route('/start/')
def start():
    service = PracticeService()
    session_repo = PracticeSessionRepository()

    practice_type = request.args.get("practice_type")
    lessons = request.args.getlist("lessons")
    total_questions = request.args.get('num_questions')
    filters = {
        'tag': practice_type,
        'question_type': 'sc_question',
        'lesson_ids': lessons
    }

    session_obj = service.create_session(filters)
    
    session_repo.set_total_questions(session_obj.id, total_questions)
    session_repo.set_current_question_idx(session_obj.id, 0)
    session_repo.set_score(session_obj.id, 0)
    session_repo.set_status(session_obj.id, 'active')

    return redirect(url_for("practice.show", session_id=session_obj.id))

@practice.route('/quiz/<session_id>/')
def show(session_id):
    service = PracticeService()
    session_repo = PracticeSessionRepository()
    session_obj = session_repo.get_object_by_id(session_id)
    strategy = PRACTICE_STRATEGIES.get(session_obj.practice_type)

    if service.practice_is_done(session_obj.id):
        return redirect(url_for('practice.results'))
    current_idx = session_repo.increase_and_get_current_idx(session_id)
    
    practice_id = session_repo.get_practice_id_by_id(session_id)
    return strategy.render_practice(practice_id, current_idx)

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
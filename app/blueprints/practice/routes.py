from flask import render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from app.models.Word import Word
from ..practice import practice
from app.extensions import csrf
from app.services import PracticeService
from app.services.practice_service import PRACTICE_STRATEGIES


@practice.route('/list')
@login_required
def show_list():
    practices = PracticeService.get_practices()
    lessons = PracticeService.get_lessons()

    return render_template('practice/list.html', practices=practices, lessons=lessons)

@practice.route('/start/')
@login_required
def start():
    try:
        practice_config = _extract_practice_config(request.args)

        session_obj = PracticeService.create_practice_session(
            user_id=current_user.id,
            practice_config=practice_config
        )

        return redirect(url_for('practice.show_question', session_id=session_obj.id))
    
    except ValueError as e:
        flash(str(e), 'error')
        print("Error occured in practice start")
        return redirect(url_for('practice.show_list'))

@practice.route('/session/<int:session_id>/question')
@login_required
def show_question(session_id):
    try:
        session_obj = PracticeService.get_user_session(current_user.id, session_id)

        if not session_obj:
            flash('Session not found', 'error')
            return redirect(url_for('practice.show_list'))
        
        if PracticeService.is_session_complete(session_obj):
            return redirect(url_for('practice.results', session_id=session_obj.id))

        question_data = PracticeService.get_current_question(session_obj)

        strategy = PRACTICE_STRATEGIES.get(session_obj.practice_type)
        if not strategy:
            flash('Invalid practice type', 'error')
            return redirect(url_for('practice.show_list'))
        
        return strategy.render_question(question_data, session_id)
    
    except Exception as e:
        flash(str(e), 'error')
        print("Error occured in practice show_question")
        return redirect(url_for('practice.show_list'))
    

@practice.route('/session/<int:session_id>/submit', methods=['POST'])
@login_required
@csrf.exempt
def submit_answer(session_id):
    try:
        session_obj = PracticeService.get_user_session(current_user.id, session_id)

        if not session_obj:
            flash('Session not found', 'error')
            return redirect(url_for('practice.show_list'))
        
        PracticeService.process_answer(session_obj, request.form)

        if PracticeService.is_session_complete(session_obj):
            return redirect(url_for('practice.results', session_id=session_id))
        
        return redirect(url_for('practice.show_question', session_id=session_id))
    
    except Exception as e:
        flash(str(e), 'error')
        print("Error occured in practice submit_answer")
        return redirect(url_for('practice.show_question', session_id=session_id))

@practice.route('/session/<int:session_id>/results')
@login_required
def results(session_id):
    try:
        session_obj = PracticeService.get_user_session(current_user.id, session_id)
        if not session_obj:
            flash('Session not found', 'error')
            return redirect(url_for('practice.show_list'))

        if not PracticeService.is_session_complete(session_obj):
            return redirect(url_for('practice.show_question'), session_id=session_id)
        
        results_data = PracticeService.get_session_results(session_obj)

        strategy = PRACTICE_STRATEGIES.get(session_obj.practice_type)
        return strategy.render_results(results_data)
    
    except Exception as e:
        flash(str(e), 'error')
        print("Error occured in practice results")
        return redirect(url_for('practice.show_list'))



def _extract_practice_config(args):
    practice_type = args.get('practice_type')
    lessons = args.getlist('lessons')
    total_questions = args.get('num_questions')
    question_type = 'text_box_question'

    if practice_type == 'article':
        question_type = 'single_choice_question'

    return {
        'practice_type': practice_type,
        'lessons': lessons,
        'total_questions': int(total_questions),
        'question_type': question_type
    }
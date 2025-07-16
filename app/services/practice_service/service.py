from app.repositories import PracticeSessionRepository, WordRepository, QuestionRepository, PracticeRepository
from app.models import Practice, PracticeSession
from app.services.practice_service import PRACTICE_STRATEGIES
import random


class PracticeService:
    
    @staticmethod
    def create_practice_session(user_id, practice_config):
        practice = PracticeService._create_practice(practice_config)
        
        session_obj = PracticeSession(
            user_id=user_id,
            practice_id=practice.id,
            practice_type=practice_config['practice_type'],
            total_questions=practice_config['total_questions'],
            current_question_idx=0,
            score=0,
            status='active'
        )
        
        PracticeSessionRepository.insert_object(session_obj)
        return session_obj
    
    @staticmethod
    def get_user_session(user_id, session_id):
        session_obj = PracticeSessionRepository.get_object_by_id(session_id)
        if session_obj and session_obj.user_id == user_id:
            return session_obj
        return None
    
    @staticmethod
    def is_session_complete(session_obj):
        return session_obj.current_question_idx >= session_obj.total_questions
    
    @staticmethod
    def get_current_question(session_obj):
        practice = PracticeRepository.get_obj_by_id(session_obj.practice_id)
        question_ids = practice.question_ids
        
        if session_obj.current_question_idx < len(question_ids):
            current_question_id = question_ids[session_obj.current_question_idx]
            question = QuestionRepository.get_question_by_id(current_question_id)
            
            return {
                'question': question,
                'question_number': session_obj.current_question_idx + 1,
                'total_questions': session_obj.total_questions,
                'session_id': session_obj.id
            }
        return None
    
    @staticmethod
    def process_answer(session_obj, form_data):
        question_data = PracticeService.get_current_question(session_obj)
        if not question_data:
            return False
        
        strategy = PRACTICE_STRATEGIES.get(session_obj.practice_type)
        if not strategy:
            return False
        
        submitted_answer = PracticeService._extract_answer_from_form(
            form_data, session_obj.practice_type
        )
        
        is_correct = strategy.check_answer(question_data['question'], submitted_answer)
        
        if is_correct:
            session_obj.score += 1
        
        if not session_obj.user_answers:
            session_obj.user_answers = []
        
        session_obj.user_answers.append({
            'question_id': question_data['question'].id,
            'submitted_answer': submitted_answer,
            'correct_answer': question_data['question'].correct_answer,
            'is_correct': is_correct
        })
        
        session_obj.current_question_idx += 1
        
        if PracticeService.is_session_complete(session_obj):
            session_obj.status = 'completed'
            from datetime import datetime, timezone
            session_obj.completed_at = datetime.now(timezone.utc)
        
        PracticeSessionRepository.update_session(session_obj)
        return is_correct
    
    @staticmethod
    def get_session_results(session_obj):
        practice = PracticeRepository.get_obj_by_id(session_obj.practice_id)
        
        return {
            'session': session_obj,
            'practice': practice,
            'score': session_obj.score,
            'total_questions': session_obj.total_questions,
            'percentage': (session_obj.score / session_obj.total_questions) * 100 if session_obj.total_questions > 0 else 0,
            'user_answers': session_obj.user_answers or []
        }
    
    @staticmethod
    def _extract_answer_from_form(form_data, practice_type):
        if practice_type == 'article':
            return form_data.get('article', '').strip()
        elif practice_type == 'plural':
            return form_data.get('plural', '').strip()
        elif practice_type == 'definition':
            return form_data.get('definition', '').strip()
        else:
            return form_data.get('answer', '').strip()
    
    @staticmethod
    def _create_practice(practice_config):
        filters = {
            'tag': practice_config['practice_type'],
            'question_type': practice_config['question_type'],
            'lesson_ids': practice_config['lessons']
        }
        
        question_repo = QuestionRepository()
        question_ids = question_repo.get_question_ids(filters)
        
        if not question_ids:
            raise ValueError(f"No questions found for practice type: {practice_config['practice_type']}")
        
        random.shuffle(question_ids)
        
        if len(question_ids) > practice_config['total_questions']:
            question_ids = question_ids[:practice_config['total_questions']]
        
        practice_object = Practice(
            practice_type=practice_config['practice_type'],
            question_type=practice_config['question_type'],
            question_ids=question_ids
        )
        
        PracticeRepository.insert_object(practice_object)
        return practice_object
    
    @staticmethod
    def get_lessons():
        ids = WordRepository.get_all_lesson_ids()
        return [{
            'id': id,
            'name': f"Lesson {id}"
        } for id in ids]

    @staticmethod
    def get_practices():
        practices = [
            {'title': 'Article Quiz', 'description': 'Choose the article of each word', 'key': "article"},
            {'title': 'Plural Quiz', 'description': 'Type the plural form of each word', 'key': "plural"},
            {'title': 'Definition Quiz', 'description': 'Type the definition of each word', 'key': "definition"}
        ] 
        return practices
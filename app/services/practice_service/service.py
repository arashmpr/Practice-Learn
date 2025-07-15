from flask_login import current_user
from app.repositories import PracticeSessionRepository, WordRepository, QuestionRepository, PracticeRepository
from app.models import Practice, PracticeSession

class PracticeService():
    def create_practice(self, filters):
        question_repo = QuestionRepository()
        question_ids = question_repo.get_question_ids(filters)
        practice_object = self.generate_practice_object(question_ids, filters)
        PracticeRepository.insert_object(practice_object)

        return practice_object

    def create_session(self, filters):
        practice = self.create_practice(filters)
        session_object = self.generate_session_object(practice.id, practice.practice_type)
        PracticeSessionRepository.insert_object(session_object)

        return session_object

    @staticmethod
    def practice_is_done(session_id):
        session_repo = PracticeSessionRepository()
        current_idx = session_repo.get_current_question_idx_by_id(session_id)
        total_questions = session_repo.get_total_questions_by_id(session_id)
        if current_idx >= total_questions:
            return True
        return False

        
    @staticmethod
    def generate_session_object(practice_id, practice_type):
        return PracticeSession(
            user_id=current_user.id,
            practice_id=practice_id,
            practice_type=practice_type
        )
    
    @staticmethod
    def generate_practice_object(question_ids, meta):
        return Practice(
            practice_type=meta['tag'],
            question_type=meta['question_type'],
            question_ids=question_ids
        )

    @staticmethod
    def get_question_data_by_practice_type(practice_type):
        question_data = ['todo']
        return question_data

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
    
    

    

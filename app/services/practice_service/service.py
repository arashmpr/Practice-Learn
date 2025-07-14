from flask_login import current_user
from app.repositories import PracticeSessionRepository, WordRepository

class PracticeService():
    def create_session(self, practice_type, num_questions, lessons):
        question_data = self.get_question_data_by_practice_type(practice_type)
        session_object = self.create_session_object(practice_type, num_questions, lessons, question_data)
        PracticeSessionRepository.insert(session_object)
        
    @staticmethod
    def create_session_object(practice_type, num_questions, lessons, question_data):
        session = {
            'user_id': current_user.id,
            'practice_type': practice_type,
            'selected_lessons': lessons,
            'total_questions': num_questions,
            'current_question_idx': 0,
            'status': 'active',
            'question_data': question_data,
            'answers': [],
            'score': 0,
        }
        return session

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

    

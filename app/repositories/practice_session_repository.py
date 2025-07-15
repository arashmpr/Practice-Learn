from app.db import db
from app.models.PracticeSession import PracticeSession

class PracticeSessionRepository():
    @staticmethod
    def insert():
        print('todo')
    
    @staticmethod
    def insert_object(object):
        db.session.add(object)
        db.session.commit()
    
    @staticmethod
    def set_total_questions(obj_id, total_questions):
        obj = db.session.get(PracticeSession, obj_id)
        if obj:
            obj.total_questions = total_questions
            db.session.commit()
    
    @staticmethod
    def set_current_question_idx(obj_id, current_question_idx):
        obj = db.session.get(PracticeSession, obj_id)
        if obj:
            obj.current_question_idx = current_question_idx
            db.session.commit()
    
    @staticmethod
    def set_status(obj_id, status):
        obj = db.session.get(PracticeSession, obj_id)
        if obj:
            obj.status = status
            db.session.commit()
        
    @staticmethod
    def set_score(obj_id, score):
        obj = db.session.get(PracticeSession, obj_id)
        if obj:
            obj.score = score
            db.session.commit()
    
    @staticmethod
    def get_object_by_id(obj_id):
        return db.session.get(PracticeSession, obj_id)
    
    @staticmethod
    def get_current_question_idx_by_id(obj_id):
        obj = db.session.get(PracticeSession, obj_id)
        return obj.current_question_idx
    
    @staticmethod
    def get_total_questions_by_id(obj_id):
        obj = db.session.get(PracticeSession, obj_id)
        return obj.total_questions
        

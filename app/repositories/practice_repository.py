from app.db import db
from app.models.Practice import Practice

class PracticeRepository():
    @staticmethod
    def insert():
        print('todo')
    
    @staticmethod
    def insert_object(object):
        db.session.add(object)
        db.session.commit()
    
    @staticmethod
    def get_obj_by_id(obj_id):
        return db.session.get(Practice, obj_id)
    
    @staticmethod
    def get_question_ids_by_id(obj_id):
        obj = db.session.get(Practice, obj_id)
        return obj.question_ids
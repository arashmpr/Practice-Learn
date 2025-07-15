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
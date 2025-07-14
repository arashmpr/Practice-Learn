from app.models.Word import Word
from app.db import db
from sqlalchemy.dialects.postgresql import insert

class WordRepository():
    @staticmethod
    def bulk_insert(values):
        stmt = insert(Word).values(values)
        stmt = stmt.on_conflict_do_nothing(constraint='uq_word_fields')
        db.session.execute(stmt)
        db.session.commit()
    
    @staticmethod
    def get_all():
        words = Word.query.all()
        return words
    
    @staticmethod
    def get_all_lesson_ids():
        uq_ids = db.session.query(Word.lesson).distinct().filter(Word.lesson.isnot(None)).all()
        sorted_ids = sorted([lesson[0] for lesson in uq_ids])
        return sorted_ids
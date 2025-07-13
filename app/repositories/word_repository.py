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
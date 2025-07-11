from app.models.Word import Word
from app.db import db
from sqlalchemy.dialects.postgresql import insert

def bulk_insert(words):
    stmt = insert(Word).values(words)
    stmt = stmt.on_conflict_do_nothing(index_elements=['word', 'lesson'])
    db.session.execute(stmt)
    db.session.commit()
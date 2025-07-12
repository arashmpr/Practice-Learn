from app.db import db
from sqlalchemy import Column, Integer, String, UniqueConstraint

class Word(db.Model):
    __tablename__ = 'word'
    id = Column(Integer, primary_key=True)
    word = Column(String(64), nullable=False)
    article = Column(String(16))
    plural = Column(String(32))
    definition = Column(String(32))
    lesson = Column(Integer, nullable=False)

    __table_args__ = (
        UniqueConstraint('word', 'lesson', name='uq_word_fields'),
    )
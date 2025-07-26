from app.db import db
from sqlalchemy import Column, Integer, String, UniqueConstraint, JSON

class Word(db.Model):
    __tablename__ = 'word'
    id = Column(Integer, primary_key=True)
    word = Column(String(64), nullable=False)
    article = Column(String(16))
    plural = Column(String(32))
    definition = Column(JSON)
    lesson = Column(Integer, nullable=False)

    example = Column(db.JSON, default=lambda: [])

    __table_args__ = (
        UniqueConstraint('word', 'lesson', name='uq_word_fields'),
    )
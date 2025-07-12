from app.db import db
from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, Text, UniqueConstraint

class SingleChoiceQuestion(db.Model):
    __tablename__ = 'single_choice_question'

    id = Column(Integer, primary_key=True)
    word_id = Column(Integer)

    tag = Column(String(32), nullable=False)
    question_type = Column(String(64), default='single_choice_question', nullable=False)
    question_text = Column(String(256), nullable=False)
    
    options = Column(db.JSON, nullable=False)
    correct_answer = Column(Text, nullable=False)

    lesson = Column(Integer)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    __table_args__ = (
        UniqueConstraint('tag', 'question_type', 'word_id', 'lesson', name='uq_word_questions_sc_fields'),
    )

class TextBoxQuestion(db.Model):
    __tablename__ = 'text_box_question'

    id = Column(Integer, primary_key=True)
    word_id = Column(Integer)

    tag = Column(String(32), nullable=False)
    question_type = Column(String(32), default='text_box_question', nullable='False')
    question_text = Column(String(256), nullable=False)

    correct_answer = Column(Text, nullable=False)

    lesson = Column(Integer)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    __table_args__ = (
        UniqueConstraint('tag', 'question_type', 'word_id', 'lesson', name='uq_word_questions_tb_fields'),
    )





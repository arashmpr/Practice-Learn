from app.db import db
from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    question_type = Column(String(64), nullable=False)
    answer_type = Column(String(64), nullable=False)
    question_text = Column(String(256), nullable=False)

    lesson = Column(Integer, nullable=False)
    

    # created_at = db.Column(db.DateTime, default=datetime.now(datetime.UTC))
    __mapper_args = {
        'polymorphic_identity': 'question',
        'polymorphic_on': question_type
    }

class SingleChoiceQuestion(Base):
    __tablename__ = 'single_choice_question'

    id = Column(Integer, primary_key=True)

    tag = Column(String(32), nullable=False)
    question_type = Column(String(64), default='single_choice_question', nullable=False)
    question_text = Column(String(256), nullable=False)
    
    options = Column(db.JSON, nullable=False)
    correct_answer = Column(Text, nullable=False)

    definition = Column(String(32))
    plural = Column(String(32))
    lesson = Column(Integer, nullable=False)

    __table_args__ = (
        UniqueConstraint('tag', 'question_type', 'question_text', 'lesson', name='uq_question_fields'),
    )

class TextBoxQuestion(Base):
    __tablename__ = 'text_box_question'

    id = Column(Integer, primary_key=True)

    tag = Column(String(32), nullable=False)
    question_type = Column(String(32), default='text_box_question', nullable='False')
    question_text = Column(String(256), nullable=False)

    correct_answer = Column(Text, nullable=False)

    definition = Column(Text)
    plural = Column(Text)
    lesson = Column(Integer, nullable=False)

    __table_args__ = (
        UniqueConstraint('tag', 'question_type', 'question_text', 'lesson', name='uq_question_fields'),
    )





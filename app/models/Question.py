from app.db import db
from datetime import datetime

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_type = db.Column(db.String(50), nullable=False)
    answer_type = db.Column(db.String(200), nullable=False)
    question_text = db.Column(db.String, nullable=False)
    

    created_at = db.Column(db.DateTime, default=datetime.now(datetime.UTC))

    __mapper_args = {
        'polymorphic_identity': 'question',
        'polymorphic_on': question_type
    }

class SingleChoiceQuestion(db.Model):
    __tablename__ = 'single_choice_question'

    id = db.Column(db.Integer, primary_key=True)
    question_type = db.Column(db.String(50), nullable=False)
    answer_type = db.Column(db.String(200), nullable=False)
    question_text = db.Column(db.String, nullable=False)
    
    options = db.Column(db.JSON, nullable=False)
    correct_answer = db.Column(db.Text, nullable=False)

    additional_info = db.Column(db.JSON)





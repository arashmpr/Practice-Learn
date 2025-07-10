from app.db import db
from datetime import datetime

practice_lesson = db.Table('practice_lesson',
    db.Column('practice_id', db.Integer, db.ForeignKey('pracice_id'), primary_key=True),
    db.Column('lesson_id', db.Integer, db.ForeignKey('lesson_id'), primary_key=True)
    )

practice_question = db.Table('practice_question',
	db.Column('practice_id', db.Integer, db.ForeignKey('practice_id'), primar_key=True),
	db.Column('question_id', db.Integer, db.ForeignKey('question_id'), primary_key=True)
	)

class Practice(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(200), nullable=False)
	description = db.Column(db.Text)
	created_at = db.Column(db.DataTime, default=datetime.now(datetime.UTC))
	has_time = db.Column(db.Boolean, default=False)
	time_limit = db.Column(db.Integer)

	lessons = db.relationship('Lesson', secondary='practice_lesson', backref='practices')
	questions = db.relationship('Question', secondary='practice_question', backref='practices')

	def to_dict(self):
		return {
			'id': self.id,
			'title': self.title,
			'description': self.description,
			'created_at': self.created_at.isoformat(),
			'has_time': self.has_time,
			'time_limit': self.time_limit,
			'lesson_ids': [lesson.id for lesson in self.lessons]
		}
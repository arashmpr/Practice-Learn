from app.db import db
from sqlalchemy import Column, Integer, String, ForeignKey

class Practice(db.Model):
	id = Column(Integer, primary_key=True)

	practice_type = Column(String, nullable=False)
	question_type = Column(String, nullable=False)

	question_ids = Column(db.JSON, nullable=False)

	def to_dict(self):
		return {
			'id': self.id,
			'session_id': self.session_id,
			'practice_type': self.practice_type,
			'question_type': self.question_type,
			'question_ids': self.question_ids
		}
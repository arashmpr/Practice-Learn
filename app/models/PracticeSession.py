from app.db import db
from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class PracticeSession(db.Model):
    __tablename__ = 'practice_session'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    practice_type = Column(String(16), nullable=False)

    selected_lessons = Column(db.JSON, nullable=False)
    total_questions = Column(Integer, nullable=False)
    current_question_idx = Column(Integer, nullable=False)

    status = Column(String(32), default='active')
    question_data = Column(db.JSON, nullable=False)
    answers = Column(db.JSON, default=lambda: [])
    score = Column(Integer, default=0)

    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    completed_at = Column(DateTime, nullable=True)

    user = relationship("User", backref="practice_sessions")


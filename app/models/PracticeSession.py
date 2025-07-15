from app.db import db
from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean

class PracticeSession(db.Model):
    __tablename__ = 'practice_session'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    practice_id = Column(Integer, ForeignKey('practice.id'), nullable=False)
    practice_type = Column(String, nullable=False)

    total_questions = Column(Integer, default=0, nullable=False)
    current_question_idx = Column(Integer, default=0, nullable=False)

    status = Column(String(32), default='active')

    has_time = Column(Boolean, default=False)
    time_limit = Column(Integer, nullable=True)

    user_answers = Column(db.JSON, default=lambda: [])
    score = Column(Integer, default=0)

    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    completed_at = Column(DateTime, nullable=True)


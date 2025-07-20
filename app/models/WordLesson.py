from app.db import db
from sqlalchemy import Column, Integer, JSON

class WordLesson(db.Model):
    id = Column(Integer, primary_key=True)
    word_ids = Column(JSON, default=lambda: [])

from flask_sqlalchemy import SQLAlchemy
from app.services.word_service import WordService

db = SQLAlchemy()

def init_db():
    db.create_all()
    print("Database tables created successfully.")

    WordService.insert_words_into_db()
    print("Words inserted into database successfully.")

    print("Database initialized successfully.")

def drop_db():
    db.drop_all()
    print("Database tables dropped successfully.")

def get_db():
    return db
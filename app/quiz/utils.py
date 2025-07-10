from app.db import db
from app.models.Word import Word

quizzes = [
    {'title': 'Article Quiz', 'description': 'Choose the article of each word', 'key': "article"},
    {'title': 'Plural Quiz', 'description': 'Type the plural form of each word', 'key': "plural"},
    {'title': 'Definition Quiz', 'description': 'Type the definition of each word', 'key': "definition"}
]

def get_lectures():
    lesson_ids = get_lesson_ids()
    return [{"id": lesson_id, "name": f"Lecture {lecture_id}"} for lecture_id in lesson_ids]


def get_lesson_ids():
    unique_lesson_ids = db.session.query(Word.lesson).distinct().filter(Word.lesson.isnot(None)).all()
    lesson_ids = sorted([lesson[0] for lesson in unique_lesson_ids])
    return lesson_ids

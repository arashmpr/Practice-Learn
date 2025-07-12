from app.db import db
from app.models.Word import Word

practices = [
    {'title': 'Article Quiz', 'description': 'Choose the article of each word', 'key': "article"},
    {'title': 'Plural Quiz', 'description': 'Type the plural form of each word', 'key': "plural"},
    {'title': 'Definition Quiz', 'description': 'Type the definition of each word', 'key': "definition"}
]

def get_lessons():
    lesson_ids = get_lesson_ids()
    print(lesson_ids)
    return [{"id": lesson_id, "name": f"Lecture {lesson_id}"} for lesson_id in lesson_ids]


def get_lesson_ids():
    unique_lesson_ids = db.session.query(Word.lesson).distinct().filter(Word.lesson.isnot(None)).all()
    lesson_ids = sorted([lesson[0] for lesson in unique_lesson_ids])
    return lesson_ids

def get_settings_info_from_request(request):
    num_questions = int(request.args.get("num_questions", 10))
    # has_definition = request.args.get("has_definition")
    # has_plural = request.args.get("has_plural")
    # has_article = request.args.get("has_article")
    # has_time_limit = request.args.get("has_time_limit")
    # time_limit = request.args.get("time_limit")

    settings_info = {
        "num_questions": num_questions,
        # "has_definition": has_definition,
        # "has_plural": has_plural,
        # "has_article": has_article,
        # "has_time_limit": has_time_limit,
        # "time_limit": time_limit
    }

    return settings_info

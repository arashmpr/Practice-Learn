from app.db import db
from app.models.Word import Word

def get_lectures():
    lecture_ids = get_lecture_ids()
    return [{"id": lecture_id, "name": f"Lecture {lecture_id}"} for lecture_id in lecture_ids]


def get_lecture_ids():
    unique_lecture_ids = db.session.query(Word.lektion).distinct().filter(Word.lektion.isnot(None)).all()
    lecture_ids = sorted([lektion[0] for lektion in unique_lecture_ids])
    return lecture_ids

import csv
from app.models.Word import Word
from app.db import db

def get_word_lessons_set(filepath):
    with open(filepath, newline='', encoding='utf-8') as f:
        word_lessons = {}
        reader = csv.DictReader(f)
        for row in reader:
            lesson = row['lesson']
            if lesson not in word_lessons:
                word_lessons[lesson] = []
            word_lessons[lesson].append(row)
        return word_lessons

def get_non_existing_lessons(lessons):
        non_existing_lessons = []
        for lesson in lessons:
            existing = Word.query.filter_by(lesson=lesson).first()
            if not existing:
                non_existing_lessons.append(lesson)
        return non_existing_lessons

def insert_words(filepath):
    word_lessons = get_word_lessons_set(filepath)
    lessons = word_lessons.keys()
    non_existing_lessons = get_non_existing_lessons(lessons)
    if len(non_existing_lessons) > 0:
        for lesson in non_existing_lessons:
            for word in word_lessons[lesson]:
                new_word = Word(
                    word = word['word'],
                    article = word['article'],
                    plural = word['plural'],
                    definition = word['definition'],
                    lesson = word['lesson']
                )
                db.session.add(new_word)
        db.session.commit()
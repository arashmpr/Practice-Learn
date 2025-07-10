import csv
from app.models.Word import Word
from app.db import db

def read_from_csv(filepath):
    with open(filepath, newline='', encoding='utf-8') as f:
        word_lessons = []
        reader = csv.DictReader(f)
        for row in reader:
            word_lessons.append((row['word'], row['lesson']))
        return word_lessons

        return word_lessons
        for row in reader:
            existing = Word.query.filter_by(word=row['word'], lektion=row['lektion']).first()
            if not existing:
                new_word = Word(
                    word = row['word'],
                    article = row['article'],
                    plural = row['plural'],
                    definition = row['definition'],
                    lektion = row['lektion']
                )

                db.session.add(new_word)
        db.session.commit()
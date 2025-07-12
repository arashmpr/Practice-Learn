import csv
from app.word.db import bulk_insert

def get_values_from_csv(filepath):
    with open(filepath, newline='', encoding='utf-8') as f:
        values = []
        reader = csv.DictReader(f)
        for line in reader:
            new_value = {
                'word': line['word'],
                'article': line['article'],
                'plural': line['plural'],
                'definition': line['definition'],
                'lesson': line['lesson']
            }
            values.append(new_value)
        return values

def insert_words(filepath):
    values = get_values_from_csv(filepath)
    bulk_insert(values)

    
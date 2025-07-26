import csv
from app.config import Config
from app.repositories.word_repository import WordRepository

config = Config()

class WordService():
    def insert_words_into_db():
        values = WordService._get_values_from_csv()
        WordRepository.bulk_insert(values)


    @staticmethod
    def _get_values_from_csv():
        values = []
        filepath = config.WORDS_FILEPATH
        with open(filepath, newline='', encoding='utf-8') as f:   
            reader = csv.DictReader(f)
            for line in reader:
                value = {
                    'word': line['word'],
                    'article': line['article'],
                    'plural': line['plural'],
                    'definition': line['definition'].split('/'),
                    'lesson': line['lesson']
                }
                values.append(value)
            return values

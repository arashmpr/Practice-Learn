from app.db import db
from app.question import db as q_db
from app.models.Question import SingleChoiceQuestion, TextBoxQuestion

class Questions:
    def generate_values(self):
        raise NotImplementedError
    
    def process(self):
        raise NotImplementedError

class ArticleTextBoxQuestions(Questions):
    def generate_values(self, words):
        questions = []
        for word in words:
            question = {
                'tag': 'article',
                'word_id': word.id,
                'question_type': 'text_box_question',
                'question_text': word.word,
                'correct_answer': word.article,
                'lesson': word.lesson,
                }
            questions.append(question)
        return questions
            
    def process(self, words):
        values = self.generate_values(words)
        constraint = 'uq_word_questions_tb_fields'
        q_db.bulk_insert(TextBoxQuestion, values, constraint)

class ArticleSingleChoiceQuestions(Questions):
    def generate_values(self, words):
        options = ['der', 'das', 'die']
        
        questions = []
        for word in words:
            question = {
                'tag': 'article',
                'word_id': word.id,
                'question_type': 'single_box_question',
                'question_text': word.word,
                'options': options,
                'correct_answer': word.article,
                'lesson': word.lesson,
                }
            questions.append(question)
        return questions
    
    def process(self, words):
        values = self.generate_values(words)
        constraint = 'uq_word_questions_sc_fields'
        q_db.bulk_insert(SingleChoiceQuestion, values, constraint)

class PluralTextBoxQuestions(Questions):
    def generate_values(self, words):
        questions = []
        for word in words:
            question = {
                'tag': 'plural',
                'word_id': word.id,
                'question_type': 'text_box_question',
                'question_text': word.word,
                'correct_answer': word.plural,
                'lesson': word.lesson,
                }
            questions.append(question)
        return questions
            
    def process(self, words):
        values = self.generate_values(words)
        constraint = 'uq_word_questions_tb_fields'
        q_db.bulk_insert(TextBoxQuestion, values, constraint)

class DefinitonTextBoxQuestions(Questions):
    def generate_values(self, words):
        questions = []
        for word in words:
            question = {
                'tag': 'definition',
                'word_id': word.id,
                'question_type': 'text_box_question',
                'question_text': word.word,
                'correct_answer': word.definition,
                'lesson': word.lesson,
                }
            questions.append(question)
        return questions
            
    def process(self, words):
        values = self.generate_values(words)
        constraint = 'uq_word_questions_tb_fields'
        q_db.bulk_insert(TextBoxQuestion, values, constraint)


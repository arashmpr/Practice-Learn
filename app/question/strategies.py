from app.db import db
from app.models.Question import SingleChoiceQuestion, TextBoxQuestion

class Questions:
    def generate(self):
        raise NotImplementedError

class ArticleTextBoxQuestions(Questions):
    def generate(self, words):
        for word in words:
            question = TextBoxQuestion(
                tag = 'article',
                question_type = 'text_box_question',
                question_text = word.word,
                correct_answer = word.article,
                definition = word.definition,
                plural = word.plural,
                lesson = word.lesson
            )
            db.session.add(question)
        db.session.commit()

class ArticleSingleChoiceQuestions(Questions):
    def generate(self, words):
        options = ['der', 'das', 'die']
        
        for word in words:
            question = SingleChoiceQuestion(
                tag = 'article',
                question_type = 'single_choice_question',
                question_text = word.word,
                options = options,
                correct_answer = word.article,
                definition = word.definition,
                plural = word.plural,
                lesson = word.lesson
            )
            db.session.add(question)
        db.session.commit()

class PluralTextBoxQuestions(Questions):
    def generate(self, words):
        for word in words:
            question = TextBoxQuestion(
                tag = 'plural',
                question_type = 'text_box_question',
                question_text = word.word,
                correct_answer = word.plural,
                definition = word.definition,
                lesson = word.lesson
            )
            db.session.add(question)
        db.session.commit()

class DefinitonTextBoxQuestions(Questions):
    def generate(self, words):
        for word in words:
            question = TextBoxQuestion(
                tag = 'definition',
                question_type = 'text_box_question',
                question_text = word.word,
                correct_answer = word.definition,
                plural = word.plural,
                lesson = word.lesson
            )
            db.session.add(question)
        db.session.commit()


from flask import render_template
from app.models.Word import Word
from app.models.Question import Question, SingleChoiceQuestion

class PracticeQuestions:
    def create(self, lessons):
        raise NotImplementedError
    
    def render_practice(self):
        raise NotImplementedError

class ArticlePractice(PracticeQuestions):
    def create(self, lessons, info):
        options = ['der', 'das', 'die']
        if lessons:
            lesson_ids = [int(lesson_id) for lesson_id in lessons]
            words = Word.query.filter(Word.lesson.in_(lesson_ids)).all()
        else:
            words = Word.query.all()
        
        for word in words:
            question = SingleChoiceQuestion(
                question_type = 'article',
                answer_type = 'single_choice_question',
                question_text = word.word
                options = options,
                correct_answer = word.article,

            )


        
PRACTICE_STRATEGIES = {
    'article': ArticlePractice()
}
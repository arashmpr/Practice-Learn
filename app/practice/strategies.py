from flask import render_template
from app.models.Word import Word
from app.models.Question import Question, SingleChoiceQuestion

class PracticeQuestions:
    def generate(self, lessons):
        raise NotImplementedError
    
    def render_practice(self):
        raise NotImplementedError

class ArticlePractice(PracticeQuestions):
    def generate(self, lessons, question_type):
        print("todo")
    def render_practice(self):
        print("todo")

        


        
PRACTICE_STRATEGIES = {
    'article': ArticlePractice()
}
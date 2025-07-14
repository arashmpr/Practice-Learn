from flask import render_template

class PracticeStrategies:
    def generate(self, lessons):
        raise NotImplementedError
    
    def render_practice(self):
        raise NotImplementedError

class ArticlePractice(PracticeStrategies):
    def generate(self, lessons, question_type):
        print("todo")
    def render_practice(self):
        print("todo")

        


        
PRACTICE_STRATEGIES = {
    'article': ArticlePractice()
}
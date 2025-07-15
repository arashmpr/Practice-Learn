from flask import render_template

class PracticeStrategies:
    def render_practice(self):
        raise NotImplementedError

class ArticleStrategy(PracticeStrategies):
    def render_practice(self):
        print("todo")

        
PRACTICE_STRATEGIES = {
    'article': ArticleStrategy()
}
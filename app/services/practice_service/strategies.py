from flask import render_template
from app.repositories import PracticeRepository, QuestionRepository

class PracticeStrategies:
    def __init__(self):
        self.practice_repo = PracticeRepository()
        self.question_repo = QuestionRepository()
    def render_practice(self):
        raise NotImplementedError

class ArticleStrategy(PracticeStrategies):
    def render_practice(self, practice_id, current_idx):
        question_ids = self.practice_repo.get_question_ids_by_id(practice_id)
        question = self.question_repo.get_question_by_id(question_ids[current_idx])
        return render_template(
            'practice/article-questions.html',
            question_num=current_idx,
            total_questions=10,
            word=question.question_text,
            definition=''
        )


        
PRACTICE_STRATEGIES = {
    'article': ArticleStrategy()
}
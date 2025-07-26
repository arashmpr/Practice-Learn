from flask import render_template
from app.repositories import PracticeRepository, QuestionRepository


class BasePracticeStrategy:
    
    def __init__(self):
        self.practice_repo = PracticeRepository()
        self.question_repo = QuestionRepository()
    
    def render_question(self, question_data, session_id):
        raise NotImplementedError()
    
    def render_results(self, results_data):
        raise NotImplementedError()
    
    def check_answer(self, question, submitted_answer):
        raise NotImplementedError()


class ArticleStrategy(BasePracticeStrategy):
    
    def render_question(self, question_data, session_id):
        question = question_data['question']
        
        return render_template(
            'practice/article-question.html',
            word=question.question_text,
            definition = '',
            question_num=question_data['question_number'],
            total_questions=question_data['total_questions'],
            session_id=session_id
        )
    
    def render_results(self, results_data):
        return render_template(
            'practice/article-results.html',
            passed=True,
            score=results_data['score'],
            total_questions=results_data['total_questions']
        )
    
    def check_answer(self, question, submitted_answer):
        return question.correct_answer.lower().strip() == submitted_answer.lower().strip()



class PluralStrategy(BasePracticeStrategy):
    
    def render_question(self, question_data, session_id):
        question = question_data['question']
        
        return render_template(
            'practice/plural-question.html',
            word=question.question_text,
            definition='',
            question_num=question_data['question_number'],
            total_questions=question_data['total_questions'],
            session_id=session_id
        )
    
    def render_results(self, results_data):
        return render_template(
            'practice/plural-results.html',
            passed=True,
            score=results_data['score'],
            total_questions=results_data['total_questions']
        )
    
    def check_answer(self, question, submitted_answer):
        correct = question.correct_answer.lower().strip()
        submitted = submitted_answer.lower().strip()
        
        if '/' in correct:
            acceptable_answers = [ans.strip() for ans in correct.split('/')]
            return submitted in acceptable_answers
        
        return correct == submitted
    


class DefinitionStrategy(BasePracticeStrategy):
    
    def render_question(self, question_data, session_id):
        question = question_data['question']
        
        return render_template(
            'practice/definition-question.html',
            word=question.question_text,
            question_num=question_data['question_number'],
            total_questions=question_data['total_questions'],
            session_id=session_id
        )
    
    def render_results(self, results_data):
        return render_template(
            'practice/definition-results.html',
            passed=True,
            score=results_data['score'],
            total_questions=results_data['total_questions']
        )
    
    def check_answer(self, question, submitted_answer):
        correct_answers = {ans.lower().strip() for ans in question.correct_answer}
        submitted = submitted_answer.lower().strip()

        return submitted in correct_answers


PRACTICE_STRATEGIES = {
    'article': ArticleStrategy(),
    'plural': PluralStrategy(),
    'definition': DefinitionStrategy()
}
from app.services.question_service.strategies import ArticleTextBoxQuestions, ArticleSingleChoiceQuestions
from app.services.question_service.strategies import PluralTextBoxQuestions
from app.services.question_service.strategies import DefinitonTextBoxQuestions
from app.services.question_service.pipeline import QuestionBankPipeline

from app.repositories.word_repository import WordRepository

class QuestionService():
    @staticmethod
    def insert_questions_into_db():
        words = WordRepository.get_all()
        
        pipeline = QuestionBankPipeline()
        
        pipeline.add_steps(ArticleTextBoxQuestions())
        pipeline.add_steps(ArticleSingleChoiceQuestions())
        pipeline.add_steps(PluralTextBoxQuestions())
        pipeline.add_steps(DefinitonTextBoxQuestions())

        pipeline.run(words)
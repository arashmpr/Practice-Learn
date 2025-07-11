from app.question.strategies import ArticleTextBoxQuestions, ArticleSingleChoiceQuestions
from app.question.strategies import PluralTextBoxQuestions
from app.question.strategies import DefinitonTextBoxQuestions
from app.question.pipeline import QuestionBankPipeline

from app.models.Word import Word

def generate_question_bank():
    words = Word.query.all()
    
    pipeline = QuestionBankPipeline()
    
    pipeline.add_steps(ArticleTextBoxQuestions())
    pipeline.add_steps(ArticleSingleChoiceQuestions())
    pipeline.add_steps(PluralTextBoxQuestions())
    pipeline.add_steps(DefinitonTextBoxQuestions())

    pipeline.run(words)
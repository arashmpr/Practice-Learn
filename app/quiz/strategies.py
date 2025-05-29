from flask import render_template
from app.models.Word import Word

class QuizStrategies:
    def render_question(self, word):
        raise NotImplementedError
    
    def check_answers(self, word, request):
        raise NotImplementedError
    
    def render_results(self, word_ids, score, total):
        raise NotImplementedError

class ArticleQuiz(QuizStrategies):
    def render_question(self, word, question_num, total_questions):
        return render_template('article-quiz.html',
                               word = word.word,
                               definition = word.definition,
                               question_num=question_num,
                               total_questions=total_questions
                            )
    
    def check_answers(self, word, request):
        return word.article.lower() == request.form['article'].lower()
    
    def render_results(self, word_ids, score, total):
        results = []
        for i, word_id in enumerate(word_ids):
            results.append({
                'word': Word.query.get(word_id).word,
                'correct_article': Word.query.get(word_id).article,
                'question_num': i + 1
            })
    
        return render_template('article_results.html', 
                            score=score,
                            total=total,
                            results=results
                            )
    
class PluralQuiz(QuizStrategies):
    def render_question(self, word, question_num, total_questions):
        return render_template('plural_quiz.html',
                               word = word.word,
                               definition = word.definition,
                               question_num=question_num,
                               total_questions=total_questions
                            )
    
    def check_answers(self, word, request):
        return word.plural.lower() == request.form['plural'].lower()
    
    def render_results(self, word_ids, score, total):
        results = []
        for i, word_id in enumerate(word_ids):
            results.append({
                'word': Word.query.get(word_id).word,
                'correct_plural': Word.query.get(word_id).plural,
                'question_num': i + 1
            })
    
        return render_template('plural_results.html', 
                            score=score,
                            total=total,
                            results=results
                            )

class DefinitionQuiz(QuizStrategies):
    def render_question(self, word, question_num, total_questions):
        return render_template('definition_quiz.html',
                               word=word.word,
                               question_num=question_num,
                               total_questions=total_questions
                            )
    
    def check_answers(self, word, request):
        return word.definition.lower() == request.form['definition'].lower()

    def render_results(self, word_ids, score, total):
        results = []
        for i, word_id in enumerate(word_ids):
            results.append({
                'word': Word.query.get(word_id).word,
                'correct_definition': Word.query.get(word_id).definition,  # Fixed: was word.article
                'question_num': i + 1
            })
    
        return render_template('definition_results.html', 
                            score=score,
                            total=total,
                            results=results
                            )
    

QUIZ_STRATEGIES = {
    'article': ArticleQuiz(),
    'plural': PluralQuiz(),
    'definition': DefinitionQuiz()
}
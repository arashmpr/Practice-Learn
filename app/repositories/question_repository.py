from app.db import db
from app.models.Question import TextBoxQuestion, SingleChoiceQuestion
from sqlalchemy.dialects.postgresql import insert


class QuestionRepository():
    def get_question_ids(self, filters):
        if filters['question_type'] == 'text_box_question':
            model = TextBoxQuestion
            
        else:
            model = SingleChoiceQuestion
        
        query = model.query
        query = self.get_queries_by_tag(query, model, filters['tag'])
        query = self.get_queries_by_lesson_ids(query, model, filters['lesson_ids'])

        question_ids = query.with_entities(model.id).all()
        return [qid[0] for qid in question_ids]
    
    @staticmethod
    def bulk_insert(model, values, constraint):
        stmt = insert(model).values(values)
        stmt = stmt.on_conflict_do_nothing(constraint=constraint)
        db.session.execute(stmt)
        db.session.commit()
    
    @staticmethod
    def get_queries_by_tag(query, model, tag):
        return query.filter(model.tag == tag)
    
    @staticmethod
    def get_queries_by_lesson_ids(query, model, lesson_ids):
        return query.filter(model.lesson_id.in_(lesson_ids))
    
    @staticmethod
    def get_question_by_id(type, obj_id):
        if type == 'single_choice_question':
            return db.session.get(SingleChoiceQuestion, obj_id)
        elif type == 'text_box_question':
            return db.session.get(TextBoxQuestion, obj_id)
        return None

        




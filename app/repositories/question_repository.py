from app.db import db
from sqlalchemy.dialects.postgresql import insert


class QuestionRepository():
    @staticmethod
    def bulk_insert(model, values, constraint):
        stmt = insert(model).values(values)
        stmt = stmt.on_conflict_do_nothing(constraint=constraint)
        db.session.execute(stmt)
        db.session.commit()
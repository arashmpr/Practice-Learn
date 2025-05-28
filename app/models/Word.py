from app.db import db

class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String, nullable=False)
    article = db.Column(db.String)
    plural = db.Column(db.String)
    definition = db.Column(db.String)
    lektion = db.Column(db.Integer)

    __table_args__ = (
        db.UniqueConstraint('word', 'lektion', name='unique_word_lektion'),
    )
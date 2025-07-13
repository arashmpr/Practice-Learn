import click 
from flask.cli import with_appcontext
from app.db import db
from app.services.word_service import WordService

@click.command('init-db')
@with_appcontext
def init_db():
    db.create_all()
    click.echo('Database tables created.')

    WordService.insert_words_into_db()
    click.echo('Words inserted into database.')

    click.echo('Database initialized successfully.')

@click.command('drop-db')
@with_appcontext
def drop_db():
    db.drop_all()
    click.echo('Database tables dropped.')


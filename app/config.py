import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Development configuration only"""

    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

    # Flask login settings
    REMEMBER_COOKIE_DURATION = 86400 # 24 hours

    # Application settings
    DEFAULT_QUESTIONS_PER_PRACTICE = int(os.getenv('QUESTIONS_PER_PRACTICE', '10'))
    DEFAULT_MAX_PRACTICE_TIME = int(os.getenv('DEFAULT_MAX_PRACTICE_TIME', '1800')) # 30 minutes
    WORDS_FILEPATH = 'data/words.csv'
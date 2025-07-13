from app import create_app
from app.db import db
from dotenv import load_dotenv
import os

def drop_database():
    """
    Reset the database by dropping all tables and recreating them.
    This will delete ALL data in the database.
    """
    load_dotenv()
    
    app = create_app(init_db=False)
    
    with app.app_context():
        print("Dropping all tables...")
        db.drop_all()
        print("All tables dropped successfully.")
        
        print("Database dropped complete!")

if __name__ == '__main__':
    confirmation = input("Are you sure you want to reset the database? This will delete ALL data. (yes/no): ")
    
    if confirmation.lower() in ['yes', 'y']:
        drop_database()
    else:
        print("Database reset cancelled.")
from app.extensions import db
    
def drop_db():
    db.drop_all()
    print("Database tables dropped successfully.")

def get_db():
    return db
# create_tables.py

from app.database import engine, Base
from app import models  # This imports your Vehicle and PatrolLog models

def create_tables():
    print("🚀 Creating tables...")
    Base.metadata.create_all(bind=engine)
    print("✅ Tables created successfully!")

if __name__ == "__main__":
    create_tables()

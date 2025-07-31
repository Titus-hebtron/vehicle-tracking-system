from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv
import os

# ✅ Load environment variables from .env
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

# ✅ Default connection string (use this if .env is missing or incorrect)
DEFAULT_DATABASE_URL = "postgresql://postgres:Pass%4012345@localhost:5432/postgres"

# ✅ Use .env if available, otherwise fallback to default
DATABASE_URL = os.getenv("DATABASE_URL", DEFAULT_DATABASE_URL)

# ✅ Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# ✅ Create session and base
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

# ✅ Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

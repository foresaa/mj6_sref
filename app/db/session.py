from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

#DATABASE_URL = os.getenv('DATABASE_URL')

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")  # Mock database URL for PDoc
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

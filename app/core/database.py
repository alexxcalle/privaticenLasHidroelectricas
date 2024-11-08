from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

metadata = MetaData()

try:
    engine = create_engine(settings.DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base(metadata=metadata)
except Exception as e:
    print(f"Error: {e}")
    raise e

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
import os

load_dotenv()

DATABASE_UTL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_UTL)

SessionLocal = sessionmaker(bind = engine , autoflush=False , autocommit=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


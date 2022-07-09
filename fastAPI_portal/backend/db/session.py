from re import S
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator

from core.config import settings

DB_URL = settings.DB_URL
engine = create_engine(DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # actual db session


def get_db() -> Generator: # during testing, we would over-ride this 'get_db' to connect to a different database
    try:
        db = SessionLocal() 
        yield db
    finally:
        db.close()
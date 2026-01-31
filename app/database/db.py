from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

SQL_DB_URL = os.getenv("SQLALCHEMY_DB_URL", "sqlite:///./app/storage/main.db")

connect_args = {}
if SQL_DB_URL.startswith('sqlite'):
    connect_args = {"check_same_thread": False}

Base = declarative_base()

engine = create_engine(
    url=SQL_DB_URL,
    echo=False,
    connect_args=connect_args
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)


def get_base():
    return Base

def get_engine():
    return engine

def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
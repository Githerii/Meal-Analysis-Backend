import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATABASE_PATH = os.path.join(BASE_DIR, "meal_analysis.db")

DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

engine = create_engine(DATABASE_URL, echo=False, future=True)
Session = sessionmaker(bind=engine, autoflush=False, future=True)
Base = declarative_base()

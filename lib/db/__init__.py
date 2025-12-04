from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///../../meal_analysis.db"  # relative to lib/db when running alembic - adjust if needed

engine = create_engine(DATABASE_URL, echo=False, future=True)
Session = sessionmaker(bind=engine, autoflush=False, future=True)
Base = declarative_base()

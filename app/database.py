from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://root:password@3.106.237.16:5432/postgres"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    from app.models import GameData

    # Ensure the schema exists
    # with engine.connect() as conn:
    #     conn.execute(text("CREATE SCHEMA IF NOT EXISTS analytics"))

    # Create tables in the specified schema
    Base.metadata.create_all(bind=engine)

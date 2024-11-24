from sqlalchemy import Column, Integer, String, Float, Boolean, Date
from app.database import Base

class GameData(Base):
    __tablename__ = "game_data"
    __table_args__ = {"schema": "analytics"}  # Use the "analytics" schema

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    app_id = Column(Integer, index=True, nullable=False)
    name = Column(String, nullable=False)
    release_date = Column(Date, nullable=False)
    required_age = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    dlc_count = Column(Integer, nullable=False)
    about_game = Column(String, nullable=False)
    supported_languages = Column(String, nullable=False)
    windows = Column(Boolean, nullable=False)
    mac = Column(Boolean, nullable=False)
    linux = Column(Boolean, nullable=False)
    positive = Column(Integer, nullable=False)
    negative = Column(Integer, nullable=False)
    score_rank = Column(Float, nullable=True)
    developers = Column(String, nullable=False)
    publishers = Column(String, nullable=True)
    categories = Column(String, nullable=True)
    genres = Column(String, nullable=False)
    tags = Column(String, nullable=True)
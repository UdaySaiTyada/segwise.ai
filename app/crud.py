from sqlalchemy.orm import Session
from app.models import GameData

def store_data(db: Session, data: list):
    for record in data:
        db_data = GameData(**record)
        db.add(db_data)
    db.commit()

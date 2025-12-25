from sqlalchemy.orm import Session
from backend.models.movements import Movement

def create_movement(db: Session, movement: Movement):
    db.add(movement)
    db.commit()
    db.refresh(movement)
    return movement

def get_movements(db: Session):
    return db.query(Movement).all()

    
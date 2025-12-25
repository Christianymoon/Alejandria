from sqlalchemy.orm import Session
from backend.models.movements import Movement
from backend.repositories.movements_repository import (
    create_movement,
    get_movements,
)


def create_new_movement(db: Session, user_id: int, publication_id: int, quantity: int, movement_type: str, notes: str):
    movement = Movement(
        user_id=user_id,
        publication_id=publication_id,
        quantity=quantity,
        movement_type=movement_type,
        notes=notes,
    )
    return create_movement(db, movement)


def list_movements(db: Session):
    return get_movements(db)

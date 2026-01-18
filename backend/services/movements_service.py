from sqlalchemy.orm import Session
from backend.models.movements import Movement
from backend.repositories.movements_repository import (
    create_movement,
    get_movements,
    get_movements_by_user,
)

#  SERVICES COMMUNICATION
from backend.services.user_service import (
    update_user_publication_service,
    get_user_service,
)


from backend.services.inventory_service import (
    update_inventory_stock_service,
)

def list_movements_by_user(db: Session, user_id: int):
    user = get_user_service(db, user_id)
    if not user:
        raise ValueError("User not found")
    return get_movements_by_user(db, user_id)

def create_new_movement(db: Session, user_id: int, publication_id: int, quantity: int, movement_type: str, notes: str):
    try:
        update_inventory_stock_service(db, publication_id, quantity)
        update_user_publication_service(db, user_id, quantity)
    except ValueError as e:
        db.rollback()
        raise e
    
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

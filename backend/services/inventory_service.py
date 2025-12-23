from sqlalchemy.orm import Session
from backend.models.inventory import Inventory
from datetime import datetime
from fastapi import HTTPException
from backend.repositories.inventory_repository import (
    get_inventory,
    get_inventory_by_id,
    get_inventory_by_publication_id,
    create_inventory,
)

def list_inventory(db: Session):
    return get_inventory(db)

def create_new_inventory(db: Session, quantity: int, publication_id: int, available: int):
    existing_inventory = get_inventory_by_publication_id(db, publication_id)
    if existing_inventory:
        raise ValueError("Inventory already exists")
    inventory = Inventory(publication_id=publication_id, total_quantity=quantity, available_quantity=available, updated_at=datetime.now())
    return create_inventory(db, inventory)


from sqlalchemy.orm import Session
from backend.models.inventory import Inventory
from datetime import datetime
from fastapi import HTTPException
from backend.repositories.inventory_repository import (
    get_inventory,
    get_inventory_by_id,
    get_inventory_by_publication_id,
    create_inventory,
    update_inventory,
)

def list_inventory(db: Session):
    return get_inventory(db)

def create_new_inventory(db: Session, quantity: int, publication_id: int, available: int):
    inventory = get_inventory_by_publication_id(db, publication_id)
    if inventory:
        raise ValueError("Inventory already exists")
    inventory = Inventory(publication_id=publication_id, total_quantity=quantity, available_quantity=available, updated_at=datetime.now())
    return create_inventory(db, inventory)

def update_inventory_stock_service(db: Session, publication_id: int, quantity: int):
    inventory = get_inventory_by_publication_id(db, publication_id)
    if not inventory:
        raise ValueError("Inventory not found")

    if quantity > inventory.available_quantity:
        raise ValueError("Not enough stock")
    inventory.available_quantity -= quantity
    return update_inventory(db, inventory)

def update_inventory_service(db: Session, inventory_id: int, quantity: int, available: int):
    inventory = get_inventory_by_id(db, inventory_id)
    if not inventory:
        raise ValueError("Inventory not found")
    inventory.total_quantity = quantity
    inventory.available_quantity = available
    return update_inventory(db, inventory)

from sqlalchemy.orm import Session
from backend.models.inventory import Inventory, InventoryHistory
from datetime import datetime
from fastapi import HTTPException
from backend.repositories.inventory_repository import (
    get_inventory,
    get_inventory_by_id,
    get_inventory_by_publication_id,
    create_inventory,
    update_inventory,
    set_inventory_history,
    get_inventory_history,
    get_inventory_history_by_publication_id
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

def update_inventory_service(db: Session, publication_id: int, quantity: int, available: int):
    inventory = get_inventory_by_publication_id(db, publication_id)
    if not inventory:
        raise ValueError("Inventory not found")
    inventory.total_quantity = quantity
    inventory.available_quantity = available
    register_inventory_service(db, inventory)
    return update_inventory(db, inventory)


def register_inventory_service(db: Session, inventory: Inventory):
    inventory_history = InventoryHistory(
        publication_id=inventory.publication_id,
        total_quantity=inventory.total_quantity,
        available_quantity=inventory.available_quantity,
        updated_at=inventory.updated_at
    )
    return set_inventory_history(db, inventory_history)

def list_inventory_history_service(db: Session):
    return get_inventory_history(db)

def list_inventory_history_by_publication_id_service(db: Session, publication_id: int):
    return get_inventory_history_by_publication_id(db, publication_id)
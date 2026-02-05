from sqlalchemy.orm import Session  # solo para validar la base de datos
from backend.models.inventory import Inventory, InventoryHistory


def get_inventory(db: Session):
    return db.query(Inventory).all()


def get_inventory_by_id(db: Session, inventory_id: int):
    return db.query(Inventory).filter(Inventory.id == inventory_id).first()


def get_inventory_by_publication_id(db: Session, publication_id: int):
    return db.query(Inventory).filter(Inventory.publication_id == publication_id).first()


def create_inventory(db: Session, inventory: Inventory):
    db.add(inventory)
    db.commit()
    db.refresh(inventory)
    return inventory


def update_inventory(db: Session, inventory: Inventory):
    db.commit()
    db.refresh(inventory)
    return inventory


def get_inventory_history(db: Session):
    return db.query(InventoryHistory).all()


def get_inventory_history_by_id(db: Session, inventory_id: int):
    return db.query(InventoryHistory).filter(InventoryHistory.inventory_id == inventory_id).all()


def set_inventory_history(db: Session, inventory: InventoryHistory):
    db.add(inventory)
    db.commit()
    db.refresh(inventory)
    return inventory

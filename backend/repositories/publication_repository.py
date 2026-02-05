from sqlalchemy.orm import Session
from backend.models.publications import Publication
from backend.models.inventory import InventoryHistory


def get_publications_from_db(db: Session):
    return db.query(Publication).all()


def get_publication_by_id_from_db(db: Session, publication_id: int):
    return db.query(Publication).filter(Publication.id == publication_id).first()


def get_publication_by_code_from_db(db: Session, publication_code: str):
    return db.query(Publication).filter(Publication.code == publication_code).first()


def get_publication_history_from_db(db: Session, inventory_id: int):
    return db.query(InventoryHistory).filter(InventoryHistory.inventory_id == inventory_id).all()


def create_publication_in_db(db: Session, publication: Publication):
    db.add(publication)
    db.commit()
    db.refresh(publication)
    return publication


def delete_publication(db: Session, publication_id: int):
    db.delete(db.query(Publication).filter(
        Publication.id == publication_id).first())
    db.commit()
    return publication_id

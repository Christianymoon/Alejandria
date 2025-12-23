from sqlalchemy.orm import Session
from backend.models.publications import Publication

def get_publications(db: Session):
    return db.query(Publication).all()

def get_publication_by_code(db: Session, publication_code: str):
    return db.query(Publication).filter(Publication.code == publication_code).first()

def create_publication(db: Session, publication: Publication):
    db.add(publication)
    db.commit()
    db.refresh(publication)
    return publication

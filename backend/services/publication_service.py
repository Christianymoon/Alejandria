from sqlalchemy.orm import Session
from backend.models.publications import Publication
from backend.repositories.publication_repository import (
    get_publications,
    get_publication_by_code,
    create_publication,
)

def list_publications(db: Session):
    return get_publications(db)

def create_new_publication(db: Session, name: str, year: int, month: int, type: str, code: str):
    existing = get_publication_by_code(db, code)
    if existing:
        raise ValueError(f"Publication with code '{code}' already exists.")
    publication = Publication(name=name, year=year, month=month, type=type, code=code)
    return create_publication(db, publication)


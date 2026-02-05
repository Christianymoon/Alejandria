from sqlalchemy.orm import Session
from backend.models.publications import Publication
from backend.repositories.publication_repository import (
    get_publications_from_db,
    get_publication_by_code_from_db,
    get_publication_by_id_from_db,
    get_publication_history_from_db,
    create_publication_in_db,
    delete_publication,
)


def get_publications_service(db: Session):
    return get_publications_from_db(db)


def get_publication_by_id_service(db: Session, publication_id: int):
    existing = get_publication_by_id_from_db(db, publication_id)
    if not existing:
        raise ValueError(
            f"Publication with id '{publication_id}' does not exist.")
    return existing


def get_publication_history_service(db: Session, publication_id: int):
    publication = get_publication_by_id_service(db, publication_id)
    if not publication:
        raise ValueError(
            f"Publication with id '{publication_id}' does not exist.")
    return get_publication_history_from_db(db, publication.inventory.id)


def create_new_publication_service(db: Session, name: str, year: int, month: int, type: str, code: str):
    existing = get_publication_by_code_from_db(db, code)
    if existing:
        raise ValueError(f"Publication with code '{code}' already exists.")
    publication = Publication(name=name, year=year,
                              month=month, type=type, code=code)
    return create_publication_in_db(db, publication)


def delete_publication_service(db: Session, publication_id: int):
    publication = get_publication_by_id_from_db(db, publication_id)
    if not publication:
        raise ValueError("Publication not exist")
    return delete_publication(db, publication.id)

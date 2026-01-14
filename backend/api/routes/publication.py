from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.services.publication_service import (
    get_publications_service,
    get_publication_by_id_service,
    create_new_publication_service)
from backend.schemas.publication_schema import PublicationCreate, PublicationResponse


router = APIRouter(
    prefix="/publications",
    tags=["publications"],
)


@router.get("/", response_model=list[PublicationResponse])
def get_publications(db: Session = Depends(get_db)):
    return get_publications_service(db)


@router.get("/view/{publication_id}", response_model=PublicationResponse)
def get_publication(publication_id: int, db: Session = Depends(get_db)):
    try:
        return get_publication_by_id_service(db, publication_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Publication not found.")


@router.post("/", response_model=PublicationResponse, status_code=status.HTTP_201_CREATED)
def create_publication(publication: PublicationCreate, db: Session = Depends(get_db)):
    try:
        return create_new_publication_service(
            db=db,
            name=publication.name,
            year=publication.year,
            month=publication.month,
            type=publication.type,
            code=publication.code
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

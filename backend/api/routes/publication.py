from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session 

from backend.core.database import get_db
from backend.services.publication_service import list_publications, create_new_publication
from backend.schemas.publication_schema import PublicationCreate, PublicationResponse


router = APIRouter(
    prefix="/publications",
    tags=["publications"],
)

@router.get("/", response_model=list[PublicationResponse])
def get_publications(db: Session = Depends(get_db)):
    return list_publications(db)

@router.post("/", response_model=PublicationResponse, status_code=status.HTTP_201_CREATED)
def create_publication(publication: PublicationCreate, db: Session = Depends(get_db)):
    try:
        return create_new_publication(
            db=db,
            name=publication.name, 
            year=publication.year, 
            month=publication.month, 
            type=publication.type, 
            code=publication.code
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
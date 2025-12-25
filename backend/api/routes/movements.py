from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.core.database import get_db
from backend.models.movements import Movement
from backend.schemas.movement_schema import MovementResponse, MovementCreate
from backend.services.movements_service import (
    create_new_movement,
    list_movements,
)

router = APIRouter(
    prefix="/movements",
    tags=["Movements"],
)


@router.get("/", response_model=list[MovementResponse])
def get_movements(db: Session = Depends(get_db)):
    return list_movements(db)


@router.post("/", response_model=MovementResponse, status_code=status.HTTP_201_CREATED)
def create_movement(movemment: MovementCreate, db: Session = Depends(get_db)):
    try:
        return create_new_movement(
            db=db,
            user_id=movemment.user_id,
            publication_id=movemment.publication_id,
            quantity=movemment.quantity,
            movement_type=movemment.movement_type,
            notes=movemment.notes
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

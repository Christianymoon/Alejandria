from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.core.database import get_db
from backend.models.movements import Movement
from backend.schemas.movement_schema import MovementCreate, MovementList
from backend.services.movements_service import (
    create_new_movement,
    list_movements,
    list_movements_by_user,
)

router = APIRouter(
    prefix="/movements",
    tags=["Movements"],
)


@router.get("/", response_model=list[MovementList])
def get_movements(db: Session = Depends(get_db)):
    return list_movements(db)


@router.get("/user/{user_id}", response_model=list[MovementList])
def get_movements_by_user(user_id: int, db: Session = Depends(get_db)):
    try:
        return list_movements_by_user(db, user_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/", response_model=MovementList, status_code=status.HTTP_201_CREATED)
def create_movement(movement: MovementCreate, db: Session = Depends(get_db)):
    try:
        return create_new_movement(
            db=db,
            user_id=movement.user_id,
            publication_id=movement.publication_id,
            quantity=movement.quantity,
            movement_type=movement.movement_type,
            notes=movement.notes
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

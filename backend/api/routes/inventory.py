from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.core.database import sessionlocal
from backend.schemas.inventory_schema import InventoryCreate, InventoryResponse, InventoryUpdate, InventoryHistoryResponse
from backend.services.inventory_service import (
    list_inventory,
    create_new_inventory,
    update_inventory_service,
    inventory_history_service,
    inventory_history_by_id_service
)

from backend.core.database import get_db

router = APIRouter(
    prefix="/inventory",
    tags=["inventory"],
)


@router.get("/", response_model=list[InventoryResponse])
def get_inventory(db: Session = Depends(get_db)):
    return list_inventory(db)


@router.get("/history", response_model=list[InventoryHistoryResponse])
def get_inventory_history(db: Session = Depends(get_db)):
    return inventory_history_service(db)


@router.get("/{inventory_id}/history", response_model=list[InventoryHistoryResponse])
def get_inventory_history_by_id(inventory_id: int, db: Session = Depends(get_db)):
    return inventory_history_by_id_service(db, inventory_id)


@router.post("/", response_model=InventoryResponse, status_code=status.HTTP_201_CREATED)
def create_inventory(inventory: InventoryCreate, db: Session = Depends(get_db)):
    try:
        return create_new_inventory(
            db=db,
            quantity=inventory.total_quantity,
            publication_id=inventory.publication_id,
            available=inventory.available_quantity
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{inventory_id}", response_model=InventoryResponse, status_code=status.HTTP_200_OK)
def update_inventory(inventory_id: int, inventory: InventoryUpdate, db: Session = Depends(get_db)):
    try:
        return update_inventory_service(
            db=db,
            inventory_id=inventory_id,
            quantity=inventory.total_quantity,
            available=inventory.available_quantity
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

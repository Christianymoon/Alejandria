from fastapi import APIRouter, Depends, HTTPException, status 
from sqlalchemy.orm import Session

from backend.core.database import sessionlocal
from backend.schemas.inventory_schema import InventoryCreate, InventoryResponse, InventoryUpdate, InventoryHistoryResponse
from backend.services.inventory_service import list_inventory, create_new_inventory, update_inventory_service, list_inventory_history_service
from backend.core.database import get_db

router = APIRouter(
    prefix="/inventory",
    tags=["inventory"],
)

@router.get("/", response_model=list[InventoryResponse])
def get_inventory(db: Session = Depends(get_db)):
    return list_inventory(db)

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

@router.post("/update", response_model=InventoryResponse, status_code=status.HTTP_200_OK)
def update_inventory(inventory: InventoryUpdate, db: Session = Depends(get_db)):
    try:
        return update_inventory_service(
            db=db,
            inventory_id=inventory.id,
            quantity=inventory.total_quantity,
            available=inventory.available_quantity
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/history", response_model=list[InventoryHistoryResponse])
def get_inventory_history(db: Session = Depends(get_db)):
    return list_inventory_history_service(db)
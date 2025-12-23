from fastapi import APIRouter, Depends, HTTPException, status 
from sqlalchemy.orm import Session

from backend.core.database import sessionlocal
from backend.schemas.inventory_schema import InventoryCreate, InventoryResponse
from backend.services.inventory_service import list_inventory, create_new_inventory
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
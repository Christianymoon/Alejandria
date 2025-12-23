from pydantic import BaseModel
from typing import Optional
from backend.schemas.inventory_schema import InventoryResponse

class PublicationResponse(BaseModel):
    id: int 
    name: str
    year: int
    month: int
    type: str
    code: str
    inventory: Optional[InventoryResponse] = None

class PublicationCreate(BaseModel):
    name: str
    year: int
    month: int
    type: str
    code: str

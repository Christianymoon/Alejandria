from pydantic import BaseModel
from datetime import datetime 

class InventoryCreate(BaseModel):
    publication_id: int
    total_quantity: int
    available_quantity: int

class InventoryResponse(BaseModel):
    id: int
    publication_id: int
    total_quantity: int
    available_quantity: int
    updated_at: datetime

    class Config:
        orm_mode = True
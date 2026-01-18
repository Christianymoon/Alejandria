from pydantic import BaseModel
from datetime import datetime 
from typing import Optional

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

    model_config = {
        "from_attributes": True
    }

class InventoryUpdate(BaseModel):
    id: int
    total_quantity: int
    available_quantity: int
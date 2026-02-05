from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class InventoryResponse(BaseModel):
    id: int
    publication_id: int
    total_quantity: int
    available_quantity: int
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }


class InventoryHistoryResponse(BaseModel):
    id: int
    inventory_id: int
    total_quantity: int
    available_quantity: int
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }


class InventoryCreate(BaseModel):
    publication_id: int
    total_quantity: int
    available_quantity: int


class InventoryUpdate(BaseModel):
    total_quantity: int
    available_quantity: int

from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from backend.schemas.user_schema import UserResponse

class MovementCreate(BaseModel):
    user_id: int
    publication_id: int
    quantity: int
    movement_type: str
    notes: Optional[str] = None

class MovementList(BaseModel):
    id: int 
    quantity: int
    movement_type: str
    timestamp: datetime
    notes: Optional[str] = None

class MovementResponse(BaseModel):
    id: int
    user_id: int
    publication_id: int
    quantity: int
    movement_type: str
    timestamp: datetime
    notes: Optional[str] = None
    user: UserResponse

from pydantic import BaseModel
from typing import Optional, TYPE_CHECKING
from datetime import datetime
from backend.schemas.common_schema import UserMini, MovementMini


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
    user: UserMini

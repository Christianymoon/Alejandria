from pydantic import BaseModel
from datetime import datetime


class UserMini(BaseModel):
    id: int
    username: str
    role_id: int
    is_active: bool


class MovementMini(BaseModel):
    quantity: int
    movement_type: str
    timestamp: datetime

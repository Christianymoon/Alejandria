from pydantic import BaseModel
from datetime import datetime


class UserMini(BaseModel):
    id: int
    username: str
    role_id: int
    is_active: bool


class PublicationMini(BaseModel):
    id: int
    name: str
    code: str

class MovementMini(BaseModel):
    publication: PublicationMini
    quantity: int
    movement_type: str
    timestamp: datetime
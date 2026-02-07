from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from backend.schemas.role_schema import RoleResponse
from backend.schemas.common_schema import MovementMini


class UserCreate(BaseModel):
    username: str
    role_id: int
    is_active: bool


class UserResponse(BaseModel):
    id: int
    username: str
    role_id: int
    total_publications: int
    role: RoleResponse
    created_at: datetime
    is_active: bool

    model_config = {
        "from_attributes": True
    }


class UserUpdate(BaseModel):
    username: str
    role_id: int
    is_active: bool

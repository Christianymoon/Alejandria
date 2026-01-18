from pydantic import BaseModel 
from datetime import datetime 
from backend.schemas.role_schema import RoleResponse

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

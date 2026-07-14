from pydantic import BaseModel, Field


class UserAdminBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=6, max_length=128)
    role_id: int = Field(..., gt=0)


class UserAdminResponse(BaseModel):
    id: int
    username: str
    role_id: int
    is_active: bool

    model_config = {
        "from_attributes": True
    }

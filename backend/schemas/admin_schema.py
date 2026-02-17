from pydantic import BaseModel

class UserAdminBase(BaseModel):
    username: str
    password: str
    role_id: int



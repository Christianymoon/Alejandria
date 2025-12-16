from pydantic import BaseModel 

class RoleResponse(BaseModel):
    name: str
    description: str | None = None
    max_publications: int

    model_config = {
        "from_attributes": True
    }
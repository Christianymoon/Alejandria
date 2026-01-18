from fastapi import APIRouter, Depends, HTTPException, status 
from sqlalchemy.orm import Session


from backend.core.database import sessionlocal
from backend.schemas.user_schema import UserCreate, UserResponse
from backend.services.user_service import list_user, create_new_user
from backend.core.database import get_db

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.get("/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return list_user(db)

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return create_new_user(
            db=db,
            username=user.username,
            role_id=user.role_id,
            is_active=user.is_active,
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
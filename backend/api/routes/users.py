from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session


from backend.core.database import sessionlocal
from backend.schemas.user_schema import UserCreate, UserResponse, UserUpdate
from backend.services.user_service import list_user, create_new_user, delete_user_by_id_service, update_user_by_id_service
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


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    try:
        delete_user_by_id_service(db, user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    try:
        return update_user_by_id_service(db, user_id, user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

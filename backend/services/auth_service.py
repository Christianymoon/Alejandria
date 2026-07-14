from backend.models.usersadmin import UserAdmin
from sqlalchemy.orm import Session
from backend.repositories.admin_repository import get_user_admin, create_user_admin
from backend.schemas.admin_schema import UserAdminBase
from backend.security.algorithms import hash_password
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi import Depends
from fastapi import HTTPException
from typing import Annotated
from backend.core.database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def register_user_admin(db: Session, user_data: UserAdminBase) -> UserAdmin:
    existing = get_user_admin(db, user_data.username)
    if existing:
        raise HTTPException(
            status_code=400, detail="Username already registered")

    hashed_pw = hash_password(user_data.password)

    new_user = UserAdmin(
        username=user_data.username,
        password=hashed_pw,
        role_id=user_data.role_id,
    )

    return create_user_admin(db, new_user)


def get_user(db: Session, username: str) -> UserAdmin:
    user = get_user_admin(db, username)
    if not user:
        raise HTTPException(
            status_code=401, detail="Invalid authentication credentials")
    return user


def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)) -> UserAdmin:
    user = get_user(db, token)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


def get_current_active_user(current_user: Annotated[UserAdmin, Depends(get_current_user)]) -> UserAdmin:
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

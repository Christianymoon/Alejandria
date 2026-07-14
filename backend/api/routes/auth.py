from fastapi import APIRouter, Depends, HTTPException, status

from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

from sqlalchemy.orm import Session
from datetime import timedelta

from backend.core.database import get_db
from backend.schemas.token_schema import Token
from backend.schemas.admin_schema import UserAdminBase, UserAdminResponse
from backend.services.auth_service import (
    get_user,
    register_user_admin,
)

from typing import Annotated
from backend.security.algorithms import hash_password, verify_password

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/signup", response_model=UserAdminResponse, status_code=status.HTTP_201_CREATED)
def register(user_data: UserAdminBase, db: Session = Depends(get_db)):
    return register_user_admin(db, user_data)


@router.post("/token")
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    user_dict = form_data.username
    if not user_dict:
        raise HTTPException(
            status_code=400, detail="Incorrect username or password")
    user = get_user(db, user_dict)
    authenticated = verify_password(form_data.password, user.password)
    if not authenticated:
        raise HTTPException(
            status_code=400, detail="Incorrect username or password")
    if not user:
        raise HTTPException(
            status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}

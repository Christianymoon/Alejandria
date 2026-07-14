from backend.schemas.token_schema import TokenData
from backend.core.database import get_db
from backend.repositories.admin_repository import get_user_admin
from backend.security.algorithms import verify_password
from backend.security.jwt import (
    ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    SECRET_KEY,
)

from datetime import datetime, timedelta, timezone
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, status
from fastapi import HTTPException
from typing import Annotated

# from jwt.exceptions import InvalidTokenError
import jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def validate_token_service(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Could not validate credentials")
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")

def create_jwt_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def auth_user_service(db: Session, username: str, password: str):
    user = get_user_admin(db, username=username)
    if not user or not verify_password(password, user.password):
        raise ValueError("Usuario o contraseña incorrectos")
    return user
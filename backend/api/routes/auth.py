from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from backend.core.database import get_db
from backend.schemas.token_schema import Token
from datetime import timedelta
from backend.services.auth_service import (
    auth_user_service, 
    create_jwt_token,
)


router = APIRouter()

@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    try:
        user = auth_user_service(db, form_data.username, form_data.password)
        access_token_expires = timedelta(minutes=30)
        access_token = create_jwt_token(data={"sub": user.username}, expires_delta=access_token_expires)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))

    return Token(access_token=access_token, token_type="bearer")
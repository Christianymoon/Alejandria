from sqlalchemy.orm import Session
from backend.models.users import User
from backend.repositories.user_repository import (
    get_users,
    get_user_by_username,
    create_user,
)

def list_user(db: Session):
    return get_users(db)

def create_new_user(db: Session, username: str, is_active: bool, role_id: int):
    existing = get_user_by_username(db, username)
    if existing:
        raise ValueError(f"User with username '{username}' already exists.")
    
    user = User(username=username, role_id=role_id, is_active=is_active)
    return create_user(db, user)
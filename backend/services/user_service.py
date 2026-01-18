from sqlalchemy.orm import Session
from backend.models.users import User
from backend.repositories.user_repository import (
    get_users,
    get_user_by_username,
    create_user,
    get_user_by_id,
    update_total_publications,
)

def list_user(db: Session):
    return get_users(db)

def get_user_service(db: Session, user_id: int):
    return get_user_by_id(db, user_id)

def update_user_publication_service(db: Session, user_id: int, quantity: int):
    user = get_user_by_id(db, user_id)
    if not user:
        raise ValueError("User not found")
    user.total_publications += quantity
    return update_total_publications(db, user)

def create_new_user(db: Session, username: str, is_active: bool, role_id: int):
    user = get_user_by_username(db, username)
    if user:
        raise ValueError(f"User with username '{username}' already exists.")
    user = User(username=username, role_id=role_id, is_active=is_active)
    return create_user(db, user)
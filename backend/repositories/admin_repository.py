from backend.models.usersadmin import UserAdmin
from sqlalchemy.orm import Session


def get_user_admin(db: Session, username: str) -> UserAdmin:
    return db.query(UserAdmin).filter(UserAdmin.username == username).first()


def create_user_admin(db: Session, user: UserAdmin) -> UserAdmin:
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

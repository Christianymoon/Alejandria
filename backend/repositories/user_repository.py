from sqlalchemy.orm import Session  # solo para validar la base de datos
from backend.models.users import User
from backend.models.movements import Movement


def get_users(db: Session):
    return db.query(User).all()


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def update_total_publications(db: Session, user: User):
    db.commit()
    db.refresh(user)
    return user


def get_user_movements(db: Session, user_id: int):
    return db.query(Movement).filter(Movement.user_id == user_id).all()


def create_user(db: Session, user: User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def delete_user_by_id(db: Session, user_id: int):
    db.delete(db.query(User).filter(User.id == user_id).first())
    db.commit()
    return user_id


def update_user(db: Session, user: User):
    db.commit()
    db.refresh(user)
    return user

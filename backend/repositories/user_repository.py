from sqlalchemy.orm import Session # solo para validar la base de datos
from backend.models.users import User

def get_users(db: Session):
    return db.query(User).all()

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def create_user(db: Session, user: User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
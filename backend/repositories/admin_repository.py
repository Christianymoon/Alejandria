from backend.models.usersadmin import UserAdmin

def get_user_admin(db: Session, username: str) -> UserAdmin:
    return db.query(UserAdmin).filter(UserAdmin.username == username).first()
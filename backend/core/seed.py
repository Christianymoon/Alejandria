from backend.core.database import sessionlocal
from backend.models.roles import Role
from backend.models.usersadmin import UserAdmin
from backend.security.algorithms import hash_password

def seed_roles():
    db = sessionlocal()

    roles = [
        {"name": "publicador", "max_publications": 2},
        {"name": "precursor", "max_publications": 5},
        {"name": "admin", "max_publications": 999},
    ]

    users = [
        {"username": "admin", "password": "secret", "role_id": 3},
    ]

    for r in roles:
        exists = db.query(Role).filter_by(name=r["name"]).first()
        if not exists:
            db.add(Role(**r))

    for u in users:
        exists = db.query(UserAdmin).filter_by(username=u["username"]).first()
        if not exists:
            db.add(UserAdmin(username=u["username"], password=hash_password(u["password"]), role_id=u["role_id"]))

    db.commit()
    db.close()

from backend.core.database import sessionlocal
from backend.models.roles import Role

def seed_roles():
    db = sessionlocal()

    roles = [
        {"name": "publicador", "max_publications": 2},
        {"name": "precursor", "max_publications": 5},
        {"name": "admin", "max_publications": 999},
    ]

    for r in roles:
        exists = db.query(Role).filter_by(name=r["name"]).first()
        if not exists:
            db.add(Role(**r))

    db.commit()
    db.close()

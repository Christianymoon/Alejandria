from fastapi import APIRouter
from backend.api.routes import users
from backend.api.routes import inventory
from backend.api.routes import publication
from backend.api.routes import movements
from backend.api.routes import auth

api_router = APIRouter()
api_router.include_router(users.router)
api_router.include_router(inventory.router)
api_router.include_router(publication.router)
api_router.include_router(movements.router)
api_router.include_router(auth.router)

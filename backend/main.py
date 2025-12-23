from fastapi import FastAPI

from backend.core.database import engine, Base 
from backend.api.router import api_router
from backend.models import roles, users, publications, inventory, movements

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Publications API"}
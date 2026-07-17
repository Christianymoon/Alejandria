import os
import sys

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.router import api_router
from backend.core.database import Base, engine
from backend.core.seed import seed_roles

from backend.core.config import FRONTEND_URL

CORS_ORIGINS_DEV = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

CORS_ORIGINS_PROD: list[str] = [
    FRONTEND_URL,
]


def _is_production() -> bool:
    if getattr(sys, "frozen", False):
        return True
    return os.getenv("ENVIRONMENT", "development").lower() == "production"


app = FastAPI()

cors_origins = CORS_ORIGINS_PROD if _is_production() else CORS_ORIGINS_DEV

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)
seed_roles()
app.include_router(api_router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Publications API"}


def run():
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")


if __name__ == "__main__":
    run()

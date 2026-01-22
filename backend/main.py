from fastapi import FastAPI
from backend.core.database import engine, Base
from backend.api.router import api_router
from backend.models import roles, users, publications, inventory, movements
from backend.core.seed import seed_roles
import uvicorn

app = FastAPI()

Base.metadata.create_all(bind=engine)
seed_roles()
app.include_router(api_router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Publications API"}


def run():
    uvicorn.run(app, host="127.0.0.1",
                port=8000, log_level="info")


if __name__ == "__main__":
    run()

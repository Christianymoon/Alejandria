import os 
import dotenv 
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_DIR = BASE_DIR / "db"
DB_DIR.mkdir(exist_ok=True)

dotenv.load_dotenv(BASE_DIR / ".env")

DATABASE_URL = os.getenv("DATABASE_URL")


if DATABASE_URL.startswith("sqlite"):
    DATABASE_URL = DATABASE_URL.replace(
        "sqlite:///database.db",
        f"sqlite:///{DB_DIR}/database.db"
    )
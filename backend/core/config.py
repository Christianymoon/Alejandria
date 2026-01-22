import os
import sys
from pathlib import Path
from dotenv import load_dotenv


def get_base_path():
    if getattr(sys, 'frozen', False):
        # Ejecutable PyInstaller
        return Path.home() / "Library" / "Application Support" / "Alejandria"
    else:
        # Desarrollo normal
        return Path(__file__).resolve().parent.parent


BASE_DIR = get_base_path()
DB_DIR = BASE_DIR / "db"
DB_DIR.mkdir(parents=True, exist_ok=True)

# Cargar .env solo en desarrollo
if not getattr(sys, 'frozen', False):
    load_dotenv(BASE_DIR / ".env")

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    DATABASE_URL = f"sqlite:///{DB_DIR}/database.db"

if DATABASE_URL.startswith("sqlite"):
    DATABASE_URL = f"sqlite:///{DB_DIR}/database.db"

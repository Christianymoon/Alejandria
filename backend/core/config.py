import os
import sys
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


def get_base_path():
    if getattr(sys, 'frozen', False):
        return Path.home() / "Library" / "Application Support" / "Alejandria"
    else:
        return Path(__file__).resolve().parent.parent


USER = os.getenv("POSTGRES_USER")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DBNAME = os.getenv("DBNAME")

DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"
FRONTEND_URL = os.getenv("FRONTEND_URL")

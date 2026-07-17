from backend.main import run
import os
import shutil
import sys
from dotenv import load_dotenv

load_dotenv()

# Standard fix for PyInstaller --noconsole / console=False
# Uvicorn (and other libs) might try to access TTY methods on sys.stdout/stderr
if sys.stdout is None:
    sys.stdout = open(os.devnull, "w")
if sys.stderr is None:
    sys.stderr = open(os.devnull, "w")


ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

if ENVIRONMENT == "production":
    print("running on production mode")
    run()
elif ENVIRONMENT == "development":
    # check if .env file exists
    print("Running in development mode")
    if not os.path.exists("backend/.env"):
        print("Error: .env file not found")
        print("Copy .env.example to .env and fill in the values")
        if os.path.exists("backend/.env.example"):
            print("Copying .env.example to .env")
            shutil.copy("backend/.env.example", "backend/.env")
        else:
            print("Error: .env.example file not found")
            sys.exit(1)

    run()

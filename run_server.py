import os
import shutil
import sys
from backend.main import run

PRODUCTION = True  # change to True when deploying

if PRODUCTION:
    run()
else:
    # check if .env file exists
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

import os 
import uvicorn 
import shutil
import sys

if __name__ == "__main__":

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

    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=True)

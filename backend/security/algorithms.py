from hashlib import sha256

SALT = "alejandria"

def hash_password(password: str) -> str:
    return sha256(SALT.encode() + password.encode()).hexdigest()

def verify_password(password: str, hash: str) -> bool:
    return hash_password(password) == hash
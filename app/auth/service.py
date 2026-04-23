from app.db.fake_db import users_db
from app.core.security import hash_password, verify_password, create_token

def register_user(username, password):
    for user in users_db:
        if user["username"] == username:
            return None

    new_user = {
        "username": username,
        "password": hash_password(password),
        "role": "user"
    }
    users_db.append(new_user)
    return new_user

def login_user(username, password):
    for user in users_db:
        if user["username"] == username:
            if verify_password(password, user["password"]):
                token = create_token({
                    "sub": username,
                    "role": user["role"]
                })
                return token
    return None

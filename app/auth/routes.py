from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import UserRegister, UserLogin
from app.auth.service import register_user, login_user

router = APIRouter()

@router.post("/register")
def register(user: UserRegister):
    result = register_user(user.username, user.password)
    if not result:
        raise HTTPException(400, "User already exists")
    return {"msg": "User registered"}

@router.post("/login")
def login(user: UserLogin):
    token = login_user(user.username, user.password)
    if not token:
        raise HTTPException(401, "Invalid credentials")
    return {"access_token": token}

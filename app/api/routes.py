from fastapi import APIRouter, Depends
from app.auth.dependencies import get_current_user, require_admin

router = APIRouter()

@router.get("/profile")
def profile(user=Depends(get_current_user)):
    return {"msg": "User profile", "user": user}

@router.get("/admin")
def admin(user=Depends(require_admin)):
    return {"msg": "Admin access granted"}

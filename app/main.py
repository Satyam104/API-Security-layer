from fastapi import FastAPI
from app.auth.routes import router as auth_router
from app.api.routes import router as api_router

app = FastAPI(title="API Security Layer")

app.include_router(auth_router)
app.include_router(api_router)

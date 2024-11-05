from fastapi import APIRouter
from app.api.v1.endpoints import outages, users

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(outages.router, prefix="/outages", tags=["outages"])
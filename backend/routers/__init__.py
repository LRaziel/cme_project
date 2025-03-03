from fastapi import APIRouter
from .users import router as users_router
from .materials import router as materials_router
from .tracking import router as tracking_router
from .failures import router as failures_router

api_router = APIRouter()
api_router.include_router(users_router)
api_router.include_router(materials_router)
api_router.include_router(tracking_router)
api_router.include_router(failures_router)
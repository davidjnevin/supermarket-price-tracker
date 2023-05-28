from fastapi import APIRouter, Depends

from app.core.config import Settings, get_settings

router = APIRouter()


@router.get("/healthcheck")
async def healthcheck(settings: Settings = Depends(get_settings)):
    return {
        "status": "ok",
        "environment": settings.environment,
        "testing": settings.testing,
    }

from fastapi import FastAPI

from app.api_routes.health_check import router as health_check_router
from app.api_routes.products import router as products_router
from app.core import config
from app.db.create_tables import create_tables


def get_application() -> FastAPI:
    app = FastAPI(title=config.PROJECT_NAME, version=config.VERSION)
    app.include_router(health_check_router, prefix=config.API_PREFIX)
    app.include_router(products_router, prefix=config.API_PREFIX)

    return app


app = get_application()


@app.on_event("startup")
def startup_event():
    create_tables()

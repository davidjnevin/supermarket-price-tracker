import logging
from functools import cache

from pydantic import AnyUrl, BaseSettings
from starlette.config import Config
from starlette.datastructures import Secret

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = "dev"
    testing: bool = bool(0)
    database_url: AnyUrl = None


@cache
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()


config = Config(".env")

PROJECT_NAME = "supermarket_price_tracker"
VERSION = "1.0.0"
API_PREFIX = "/api"

SECRET_KEY = config(
    "SECRET_KEY", cast=Secret, default="unsafesecretkey_please_CHANGEME"
)

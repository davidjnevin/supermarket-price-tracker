import os
from typing import AsyncIterator

import httpx
import pytest_asyncio

from app import main
from app.core.config import Settings, get_settings


async def get_settings_override():
    return Settings(testing=1, database_url=os.environ.get("DATABASE_TEST_URL"))


@pytest_asyncio.fixture()
async def test_client() -> AsyncIterator[httpx.AsyncClient]:
    # set up
    main.app.dependency_overrides[get_settings] = get_settings_override
    # Create a test_app that uses the startup and shutdown on_events
    async with httpx.AsyncClient(
        app=main.app, base_url="http://testserver"
    ) as test_client:
        # testing
        yield test_client

    # tear down

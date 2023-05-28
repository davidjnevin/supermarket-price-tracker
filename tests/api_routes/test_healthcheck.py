import httpx
import pytest

from app import main  # noqa : F401


@pytest.mark.asyncio
async def test_healthcheck(test_client: httpx.AsyncClient) -> None:
    response = await test_client.get("/api/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "environment": "dev", "testing": True}

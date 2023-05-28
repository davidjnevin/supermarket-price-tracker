import httpx
import pytest

from app import main  # noqa : F401


@pytest.mark.asyncio
async def test_create_product(test_client: httpx.AsyncClient) -> None:
    response = await test_client.post("/api/products")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "environment": "dev", "testing": True}

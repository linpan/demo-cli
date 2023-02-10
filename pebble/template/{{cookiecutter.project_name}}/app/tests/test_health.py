import pytest
from httpx import AsyncClient

from app.main import app

# All test coroutines will be treated as marked.
pxytestmark = pytest.mark.asyncio


async def test_health():
    """
    Test health endpoint.
    """
    async with AsyncClient(app=app, base_url="http://localhost:8005") as ac:
        response = await ac.get("/health")
    assert response.status_code == 200
    assert response.json() == {"message": "ok"}

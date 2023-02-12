import pytest
from typing import Any, AsyncGenerator

from fastapi import FastAPI
# from asyncmock import AsyncMock
from httpx import AsyncClient
from app.main import app as fastapi_app

@pytest.fixture
def anyio_backend():
    return 'asyncio'


@pytest.fixture
async def text_client(
    fastapi_app: FastAPI,
    anyio_backend: Any,
) -> AsyncGenerator[AsyncClient, None]:
    """
    Fixture that creates client for requesting server.

    :param anyio_backend:
    :param fastapi_app: the application.
    :yield: client for the app.
    """
    async with AsyncClient(app=fastapi_app, base_url="http://test") as ac:
        yield ac

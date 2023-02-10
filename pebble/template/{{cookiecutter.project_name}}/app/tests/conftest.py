import pytest
# from asyncmock import AsyncMock

@pytest.fixture
def anyio_backend():
    return 'asyncio'

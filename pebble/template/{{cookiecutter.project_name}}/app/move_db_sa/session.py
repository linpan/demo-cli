from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# create asyncio engine
async_engine = create_async_engine(f"postgresql+asyncpg:{settings.pg_native_url}", echo=True)

async_session = sessionmaker(
    async_engine, class_=AsyncSession,
)


# Dependency
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session

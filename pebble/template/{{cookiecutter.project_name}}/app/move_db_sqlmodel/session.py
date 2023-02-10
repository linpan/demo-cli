from sqlalchemy.orm import sessionmaker
from core.config import settings
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import SQLModel

# see https://sqlmodel.tiangolo.com/tutorial/create-db-and-table/
connect_args = {"check_same_thread": False}

engine = create_async_engine(
    settings.DB_URI,
    echo=True,
    future=True)

# sync_session = se
async_session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def init_db():
    async with engine.begin() as conn:
        # await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session

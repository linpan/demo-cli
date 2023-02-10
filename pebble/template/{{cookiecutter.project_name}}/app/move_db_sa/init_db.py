import asyncio
from sqlalchemy import MetaData
from app.core.config import settings
from app.db.base import Base
from app.db.session import async_engine

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

meta = MetaData(naming_convention=convention)

async def async_main():
    async with async_engine.begin() as conn:
        await conn.run_sync(meta.create_all)

if __name__ == '__main__':
    asyncio.run(async_main())

from tortoise import Tortoise
from app.core.config import settings

async def get_db()-> None:
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['app.models']}
    )
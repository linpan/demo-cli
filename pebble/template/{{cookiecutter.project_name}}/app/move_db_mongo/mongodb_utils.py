import logging

from motor.motor_asyncio import AsyncIOMotorClient
from core.config.settings import settings
from .mongodb import db


async def connect_to_mongo():
    logging.info("连接数据库中...")
    db.client = AsyncIOMotorClient("mongodb://localhost/?retryWrites=true&w=majority")
    logging.info("连接数据库成功！")


async def close_mongo_connection():
    logging.info("关闭数据库连接...")
    db.client.close()
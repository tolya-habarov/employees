import logging

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection
from pymongo.errors import ConnectionFailure

from app.config import config

logger = logging.getLogger(__name__)
db = AsyncIOMotorClient(config.MONGO_URL)


async def get_db():
    return db


async def get_collection(db_name: str, collection: str) -> AsyncIOMotorCollection:
    db = await get_db()
    return db[db_name][collection]


async def connect():
    try:
        await db.admin.command('ping')
        logger.info('Mongo successfully connected')
    except ConnectionFailure:
        logger.error('Mongo connect fail')


def disconnect():
    if db is not None:
        db.close()
        logger.error('Mongo disconnected')

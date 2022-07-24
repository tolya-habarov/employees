from typing import Dict, Sequence

from motor.motor_asyncio import AsyncIOMotorCollection


async def get_employees(
    collection: AsyncIOMotorCollection,
    min_age: int,
    max_age: int,
) -> Sequence[Dict]:
    cursor = collection.find({'age': {'$gte': min_age, '$lte': max_age}})
    return await cursor.to_list(None)

from typing import List

from app.employees import crud, schemas
from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorCollection

from app.config import config
from app.db import get_collection

router = APIRouter()


async def get_employee_collection():
    return await get_collection(config.MONGO_DB, 'employees')


@router.post(
    '/',
    description='Get employees by some fields',
    response_model=List[schemas.EmployeeOut],
)
async def get_employees(
    *,
    col: AsyncIOMotorCollection = Depends(get_employee_collection),
    query: schemas.EmployeeFilter,
):
    employees = await crud.get_employees(col, **query.dict())
    return employees

import datetime as dt
from typing import Dict, List, Optional, Sequence

from motor.motor_asyncio import AsyncIOMotorCollection


async def get_employees(collection: AsyncIOMotorCollection, **kwargs) -> Sequence[Dict]:
    """Get employees by filters. See EmployeeFilter for kwargs"""
    filter_ = _get_filter(**kwargs)
    cursor = collection.find(filter_)
    return await cursor.to_list(None)


def _get_filter(
    min_age: Optional[int] = None,
    max_age: Optional[int] = None,
    companies: Optional[List[str]] = None,
    start_join_date: Optional[dt.datetime] = None,
    end_join_date: Optional[dt.datetime] = None,
    job_titles: Optional[List[str]] = None,
    genders: Optional[List[str]] = None,
    min_salary: Optional[int] = None,
    max_salary: Optional[int] = None,
):

    filter_ = dict()

    if any({min_age, max_age}):
        filter_['age'] = age = dict()
        if min_age is not None:
            age['$gte'] = min_age
        if max_age is not None:
            age['$lte'] = max_age

    if companies:
        filter_['company'] = {'$in': companies}

    if any({start_join_date, end_join_date}):
        filter_['join_date'] = join_date = dict()
        if start_join_date is not None:
            join_date['$gte'] = start_join_date
        if end_join_date is not None:
            join_date['$lte'] = end_join_date

    if job_titles:
        filter_['job_title'] = {'$in': job_titles}

    if genders:
        filter_['gender'] = {'$in': genders}

    if any({min_salary, max_salary}):
        filter_['salary'] = salary = dict()
        if min_salary is not None:
            salary['$gte'] = min_salary
        if max_salary is not None:
            salary['$lte'] = max_salary

    return filter_

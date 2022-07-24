import datetime as dt
from typing import List, Literal, Optional

from pydantic import BaseModel, EmailStr

Gender = Literal['male', 'female', 'other']


class EmployeeOut(BaseModel):
    name: str
    email: EmailStr
    age: int
    company: str
    join_date: dt.datetime
    job_title: str
    gender: Gender
    salary: int


class EmployeeFilter(BaseModel):
    min_age: Optional[int] = None
    max_age: Optional[int] = None

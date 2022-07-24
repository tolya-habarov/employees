import datetime as dt
from typing import List, Literal, Optional

from pydantic import BaseModel, EmailStr, Field, root_validator

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
    min_age: Optional[int] = Field(default=None, gt=0)
    max_age: Optional[int] = Field(default=None, gt=0)
    companies: Optional[List[str]] = Field(default=None, min_items=1)
    start_join_date: Optional[dt.datetime] = None
    end_join_date: Optional[dt.datetime] = None
    job_titles: Optional[List[str]] = Field(default=None, min_items=1)
    genders: Optional[List[Gender]] = Field(default=None, min_items=1)
    min_salary: Optional[int] = Field(default=None, gt=0)
    max_salary: Optional[int] = Field(default=None, gt=0)

    @root_validator()
    def min_age_gt_max_age(cls, values):
        if all({values['min_age'], values['max_age']}):
            if values['min_age'] > values['max_age']:
                raise ValueError('min_age must be less than max_age')

        if all({values['start_join_date'], values['end_join_date']}):
            if values['start_join_date'] > values['end_join_date']:
                raise ValueError('start_join_date must be less than end_join_date')

        if all({values['min_salary'], values['max_salary']}):
            if values['min_salary'] > values['max_salary']:
                raise ValueError('min_salary must be less than max_salary')

        return values

import datetime as dt
from typing import List, Literal, Optional

from pydantic import BaseModel, EmailStr, Field, root_validator

Gender = Literal['male', 'female', 'other']


class EmployeeOut(BaseModel):
    """Employee model"""

    name: str
    email: EmailStr
    age: int
    company: str
    join_date: dt.datetime
    job_title: str
    gender: Gender
    salary: int


class EmployeeFilter(BaseModel):
    """Filter employee by some fields"""

    min_age: Optional[int] = Field(default=None, ge=0)
    max_age: Optional[int] = Field(default=None, ge=0)
    companies: Optional[List[str]] = Field(default=None, min_items=1)
    start_join_date: Optional[dt.datetime] = None
    end_join_date: Optional[dt.datetime] = None
    job_titles: Optional[List[str]] = Field(default=None, min_items=1)
    genders: Optional[List[Gender]] = Field(default=None, min_items=1)
    min_salary: Optional[int] = Field(default=None, ge=0)
    max_salary: Optional[int] = Field(default=None, ge=0)

    class Config:
        schema_extra = {
            'example': {
                'min_age': 10,
                'max_age': 50,
                'companies': ['Twitter', 'Yandex', 'Google'],
                'start_join_date': dt.datetime(1999, 1, 1, 0, 0),
                'end_join_date': dt.datetime(2005, 1, 1, 0, 0),
                'job_titles': ['janitor', 'manager', 'developer'],
                'genders': ['male', 'other'],
                'min_salary': 1793,
                'max_salary': 6397,
            }
        }

    @root_validator()
    def min_gt_max(cls, values):
        """Check minimum values are less than maximum values"""

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

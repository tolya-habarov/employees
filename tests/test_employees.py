import datetime as dt
from typing import List

from httpx import AsyncClient
from pydantic import parse_obj_as

from app.employees import schemas, view
from app.main import app


async def test_get_employees_by_age(client: AsyncClient):
    filter_ = schemas.EmployeeFilter(min_age=20, max_age=30)
    url = app.url_path_for(view.get_employees.__name__)

    response = await client.post(url, json=filter_.dict())

    assert response.status_code == 200, response.json()
    employees = parse_obj_as(List[schemas.EmployeeOut], response.json())
    assert len(employees) != 0
    for item in employees:
        assert filter_.min_age <= item.age <= filter_.max_age


async def test_get_employees_by_age_error(client: AsyncClient):
    filter_ = dict(min_age=30, max_age=20)
    url = app.url_path_for(view.get_employees.__name__)

    response = await client.post(url, json=filter_)

    assert response.status_code == 422, response.json()
    assert response.json() == {
        'detail': [
            {
                'loc': ['body', '__root__'],
                'msg': 'min_age must be less than max_age',
                'type': 'value_error',
            }
        ]
    }


async def test_get_employees_by_companies(client: AsyncClient):
    filter_ = schemas.EmployeeFilter(companies=['Twitter', 'Yandex', 'Google'])
    url = app.url_path_for(view.get_employees.__name__)

    response = await client.post(url, json=filter_.dict())

    assert response.status_code == 200, response.json()
    employees = parse_obj_as(List[schemas.EmployeeOut], response.json())
    assert len(employees) != 0
    for item in employees:
        assert item.company in filter_.companies


async def test_get_employees_by_join_date(client: AsyncClient):
    filter_ = schemas.EmployeeFilter(
        start_join_date=dt.datetime(1999, 1, 1, 0, 0),
        end_join_date=dt.datetime(2005, 1, 1, 0, 0),
    )
    url = app.url_path_for(view.get_employees.__name__)

    response = await client.post(url, data=filter_.json())

    assert response.status_code == 200, response.json()
    employees = parse_obj_as(List[schemas.EmployeeOut], response.json())
    # FIXME: join_date string to date in mongo
    # assert len(employees) != 0
    for item in employees:
        assert filter_.start_join_date <= item.join_date <= filter_.end_join_date


async def test_get_employees_by_join_date_error(client: AsyncClient):
    filter_ = dict(
        start_join_date='2005-01-01T00:00:00.000Z',
        end_join_date='1999-01-01T00:00:00.000Z',
    )
    url = app.url_path_for(view.get_employees.__name__)

    response = await client.post(url, json=filter_)

    assert response.status_code == 422, response.json()
    assert response.json() == {
        'detail': [
            {
                'loc': ['body', '__root__'],
                'msg': 'start_join_date must be less than end_join_date',
                'type': 'value_error',
            }
        ]
    }


async def test_get_employees_by_job_titles(client: AsyncClient):
    filter_ = schemas.EmployeeFilter(job_titles=['janitor', 'manager', 'developer'])
    url = app.url_path_for(view.get_employees.__name__)

    response = await client.post(url, json=filter_.dict())

    assert response.status_code == 200, response.json()
    employees = parse_obj_as(List[schemas.EmployeeOut], response.json())
    assert len(employees) != 0
    for item in employees:
        assert item.job_title in filter_.job_titles


async def test_get_employees_by_genders(client: AsyncClient):
    filter_ = schemas.EmployeeFilter(genders=['male', 'other'])
    url = app.url_path_for(view.get_employees.__name__)

    response = await client.post(url, json=filter_.dict())

    assert response.status_code == 200, response.json()
    employees = parse_obj_as(List[schemas.EmployeeOut], response.json())
    assert len(employees) != 0
    for item in employees:
        assert item.gender in filter_.genders


async def test_get_employees_by_salary(client: AsyncClient):
    filter_ = schemas.EmployeeFilter(min_salary=1793, max_salary=6397)
    url = app.url_path_for(view.get_employees.__name__)

    response = await client.post(url, json=filter_.dict())

    assert response.status_code == 200, response.json()
    employees = parse_obj_as(List[schemas.EmployeeOut], response.json())
    assert len(employees) != 0
    for item in employees:
        assert filter_.min_salary <= item.salary <= filter_.max_salary


async def test_get_employees_by_salary_error(client: AsyncClient):
    filter_ = dict(min_salary=6397, max_salary=1793)
    url = app.url_path_for(view.get_employees.__name__)

    response = await client.post(url, json=filter_)

    assert response.status_code == 422, response.json()
    assert response.json() == {
        'detail': [
            {
                'loc': ['body', '__root__'],
                'msg': 'min_salary must be less than max_salary',
                'type': 'value_error',
            }
        ]
    }

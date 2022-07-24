from typing import List

from fastapi.testclient import TestClient
from pydantic import parse_obj_as

from app.employees import view, schemas
from app.main import app

def test_get_employees(client: TestClient):
    filter_ = schemas.EmployeeFilter(min_age=20, max_age=30)
    url = app.url_path_for(view.get_employees.__name__)

    response = client.post(url, json=filter_.dict())
    assert response.status_code == 200, response.json()
    employees = parse_obj_as(List[schemas.EmployeeOut], response.json())
    assert len(employees) != 0

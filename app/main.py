from fastapi import FastAPI

from app.db import connect, disconnect
from app.employees.view import router as employees_router

app = FastAPI(title='employees api')
app.add_event_handler("startup", connect)
app.add_event_handler("shutdown", disconnect)

app.include_router(employees_router, prefix='/employees')

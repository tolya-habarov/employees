from fastapi import FastAPI

from app.db import connect, disconnect

app = FastAPI(title='employees api')
app.add_event_handler("startup", connect)
app.add_event_handler("shutdown", disconnect)

from pydantic import BaseSettings


class Config(BaseSettings):
    MONGO_DB: str
    MONGO_URL: str


config = Config(_env_file='.env')

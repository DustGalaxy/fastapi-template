from pydantic import Field
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    DB_HOST: str = Field(alias='DB_HOST')
    DB_PORT: str = Field(alias='DB_HOST')
    DB_PASS: str = Field(alias='DB_PASS')
    DB_USER: str = Field(alias='DB_USER')
    DB_NAME: str = Field(alias='DB_NAME')

    SESSION_LIVE_TIME: int = Field(alias='SESSION_LIVE_TIME')


from pydantic import Field
from pydantic_settings import BaseSettings
from dotenv import dotenv_values, find_dotenv, load_dotenv

env_path = find_dotenv(".env")
load_dotenv(env_path)
config = dotenv_values(".env")


class ConfigClass(BaseSettings):
    DB_HOST: str = Field(alias="DB_HOST")
    DB_PORT: str = Field(alias="DB_PORT")
    DB_PASS: str = Field(alias="DB_PASS")
    DB_USER: str = Field(alias="DB_USER")
    DB_NAME: str = Field(alias="DB_NAME")

    SESSION_LIVE_TIME: int = Field(alias="SESSION_LIVE_TIME")

    DB_URL: str | None = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.DB_URL = f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


Config = ConfigClass.model_validate(config)

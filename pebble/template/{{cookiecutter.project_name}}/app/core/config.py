from pathlib import Path
from typing import Optional

from pydantic import BaseSettings, HttpUrl, MongoDsn

#
# see https://github.com/IHosseini083/Shortify/blob/main/shortify/app/core/config.py

PROJECT_DIR = Path(__file__).parent.parent.parent

# This adds support for 'mongodb+srv' connection schemas when using e.g. MongoDB Atlas
MongoDsn.allowed_schemes.add("mongodb+srv")

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "{{cookiecutter.project_name}}"
    SENTRY_DSN: Optional[HttpUrl] = None
    VERSION = 2
    DB_URI = "postgresql+asyncpg://hiro:rcts2020@localhost:5432/mock"
    USE_CORRELATION_ID: bool = True
    #
    POSTGRES_USER = 'hiro'
    POSTGRES_PASSWORD = "rcts2020"
    POSTGRES_SERVER = 'localhost'
    POSTGRES_PORT = 5432
    POSTGRES_DB = 'mock'

    @property
    def pg_native_url(self) -> str:
        return f"//{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    class Config:
        case_sensitive = True
        env_file = ".env"
        # Place your .env file under this path
        # env_file = "shortify/.env"
        # env_prefix = "SHORTIFY_"


settings = Settings()


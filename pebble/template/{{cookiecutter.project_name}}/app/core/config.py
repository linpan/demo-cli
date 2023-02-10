import datetime
from pathlib import Path
from typing import Optional

import pytz
from pydantic import BaseSettings, HttpUrl, MongoDsn

#
# see https://github.com/IHosseini083/Shortify/blob/main/shortify/app/core/config.py

PROJECT_DIR = Path(__file__).parent.parent.parent


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DEBUG: bool = True
    PROJECT_NAME: str = "{{cookiecutter.project_name}}"
    SENTRY_DSN: Optional[HttpUrl] = None
    ENVIRONMENT: str = "dev"
    VERSION: int = 2
    DB_URI = "postgresql+asyncpg://hiro:rcts2020@localhost:5432/mock"
    USE_CORRELATION_ID: bool = True

    USE_CORRELATION_ID: bool = True
    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_FILE_PATH: str = "logs/shortify.log"

    POSTGRES_USER: str = 'hiro'
    POSTGRES_PASSWORD: str = "rcts2020"
    POSTGRES_SERVER: str = 'localhost'
    POSTGRES_PORT:int= 5432
    POSTGRES_DB :str = 'mock'
    TIME_ZONE: datetime.tzinfo = pytz.timezone("UTC")

    # Database
    MONGODB_URI: MongoDsn = "mongodb://localhost:27017/"  # type: ignore[assignment]

    # warning in production must be disabled
    REDOC_URL: Optional[str] = "/redoc"
    DOCS_URL: Optional[str] = "/docs"

    @property
    def pg_native_url(self) -> str:
        return f"//{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    class Config:
        env_file = ".env"
        # Place your .env file under this path
        # env_file = "short/.env"
        # env_prefix = "short_"


settings = Settings()

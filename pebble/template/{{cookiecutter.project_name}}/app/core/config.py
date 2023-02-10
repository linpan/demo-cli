import datetime
from pathlib import Path
from typing import Optional

import pytz
from pydantic import BaseSettings, HttpUrl, MongoDsn, PostgresDsn, KafkaDsn, RedisDsn, AmqpDsn

#
# see https://github.com/IHosseini083/Shortify/blob/main/shortify/app/core/config.py

PROJECT_DIR = Path(__file__).parent.parent.parent


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DEBUG: bool = True
    PROJECT_NAME: str = "{{cookiecutter.project_name}}"

    ENVIRONMENT: str = "dev"
    VERSION: int = 2

    USE_CORRELATION_ID: bool = True

    TIME_ZONE: datetime.tzinfo = pytz.timezone("UTC")

    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_FILE_PATH: str = "logs/prod.log"

    # postgres database
    POSTGRES_URL: PostgresDsn = "postgresql+asyncpg://hiro:rcts2020@localhost:5432/mock"

    # MONGODB Database
    MONGODB_URI: MongoDsn = "mongodb://localhost:27017/"

    # MySQL Database
    MYSQL_URI: str = "mysql://username:password@server/db"
    # Redis Database
    REDIS_URL: RedisDsn = "redis://localhost:6379/0"

    # Kafka Database
    KAFKA_BROKER: KafkaDsn = "kafka://localhost:9092"
    # RabbitMQ Queue
    RABBIT_URI: AmqpDsn = "amqp://guest:guest@rabbitmq:5672//"

    # warning in production must be disabled
    # Sentry
    SENTRY_DSN: Optional[HttpUrl] = None

    REDOC_URL: Optional[str] = "/redoc"
    DOCS_URL: Optional[str] = "/docs"

    class Config:
        env_file = ".env"
        # Place your .env file under this path
        # env_file = "short/.env"
        # env_prefix = "short_"


settings = Settings()

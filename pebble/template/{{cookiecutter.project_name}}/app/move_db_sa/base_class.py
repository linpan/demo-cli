# https://blog.yasking.org/a/postgresql-partitioning.html
# todo -- 加载uuid扩展
# CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import registry
from sqlalchemy import Column, Integer, UUID, text, BigInteger
from sqlalchemy.dialects.postgresql import UUID


@as_declarative()
class Base:
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    # id = Column(Integer, primary_key=True)
    # id = Column(BigInteger, primary_key=True)
    id = Column(UUID(as_uuid=True), server_default=text("gen_random_uuid()"), primary_key=True)

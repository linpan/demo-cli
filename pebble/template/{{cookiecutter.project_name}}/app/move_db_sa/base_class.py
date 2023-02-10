from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import registry
from sqlalchemy import Column, Integer
mapper_registry = registry()


@mapper_registry.as_declarative_base()
class Base:
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)

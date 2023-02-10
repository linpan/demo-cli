from datetime import datetime
from typing import TYPE_CHECKING, List

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import selectinload
from sqlalchemy import func
from app.db.base_class import Base
from .item import Item
if TYPE_CHECKING:
    from .item import Item  # noqa: F401


class User(Base):
    __tablename__ = "a"

    id: Mapped[int] = mapped_column(primary_key=True)
    data: Mapped[str]
    create_date: Mapped[datetime] = mapped_column(server_default=func.now())
    bs: Mapped[List["Item"]] = relationship(lazy="raise")

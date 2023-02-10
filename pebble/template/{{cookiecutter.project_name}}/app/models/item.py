from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import selectinload

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class Item(Base):
    __tablename__ = "b"
    id: Mapped[int] = mapped_column(primary_key=True)
    a_id: Mapped[int] = mapped_column(ForeignKey("a.id"))
    data: Mapped[str]

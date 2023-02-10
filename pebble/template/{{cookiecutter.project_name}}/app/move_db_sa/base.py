# Import all the models, so that Base has them before being
# imported by Alembic
import pytz
from app.models.item import Item  # noqa
from app.models.user import User  # noqa

from app.db.base_class import Base  # noqa

from sqlalchemy import Column, DateTime
from datetime import datetime
from app.core.config import settings


tz = settings.TIME_ZONE

class TimestampMixin:
    created_at = Column(DateTime, server_default=datetime.now(tz=tz), nullable=False)
    updated_at = Column(DateTime, server_default=datetime.now(tz=tz), server_onupdate=datetime.now(tz=tz),
                        nullable=False)


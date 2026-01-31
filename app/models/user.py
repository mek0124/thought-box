from sqlalchemy import Column, String, Boolean, ForeignKey, UUID, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from uuid import uuid4

from ..database.db import get_base


Base = get_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(
        UUID,
        primary_key=True,
        index=True,
        default=lambda: uuid4()
    )

    username = Column(
        String,
        index=True,
        unique=True
    )

    created_at = Column(
        DateTime,
        index=True,
        default=lambda: datetime.now()
    )

    updated_at = Column(
        DateTime,
        index=True,
        default=lambda: datetime.now(),
        onupdate=datetime.now
    )

    is_active = Column(
        Boolean,
        index=True,
        default=False
    )

    entries = relationship("Entry", back_populates="user", cascade="all, delete-orphan")
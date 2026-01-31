from sqlalchemy import Column, String, ForeignKey, UUID, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from uuid import uuid4

from ..database.db import get_base


Base = get_base()


class Entry(Base):
    __tablename__ = 'entries'

    id = Column(
        UUID,
        primary_key=True,
        index=True,
        default=lambda: uuid4()
    )

    title = Column(
        String,
        index=True,
        unique=True,
        nullable=False
    )

    content = Column(String, nullable=False)

    created_at = Column(
        DateTime,
        index=True,
        default=lambda: datetime.now()
    )

    updated_at = Column(
        DateTime,
        index=True,
        default=lambda: datetime.now(),
        onupdate=lambda: datetime.now()
    )

    user_id = Column(
        UUID,
        ForeignKey('users.id'),
        nullable=False
    )

    user = relationship("User", back_populates="entries")
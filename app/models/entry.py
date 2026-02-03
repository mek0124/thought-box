from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime
from uuid import uuid4

from ..database.db import get_base


Base = get_base()


class Entry(Base):
    __tablename__ = 'entries'

    id = Column(
        Integer,
        primary_key = True,
        index = True,
        autoincrement = True
    )

    title = Column(
        String,
        index = True,
        unique = True
    )

    content = Column(String)

    created_at = Column(
        DateTime,
        index = True,
        default = lambda: datetime.now()
    )

    update_at = Column(
        DateTime,
        index = True,
        default = lambda: datetime.now(),
        onupdate = lambda: datetime.now()
    )
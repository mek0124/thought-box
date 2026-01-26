from sqlalchemy import Column, Integer, String, UUID, DateTime
from datetime import datetime
from uuid import uuid4

from ..database.db import get_base


Base = get_base()


class EntryModel(Base):
    __tablename__ = 'entries'

    id = Column(UUID, index = True, primary_key = True, default = lambda: uuid4())
    title = Column(String, index = True, unique = True)
    content = Column(String)
    created_at = Column(DateTime, index=True, default=lambda:datetime.now())
    updated_at = Column(DateTime, index=True, default=lambda:datetime.now(), onupdate=lambda:datetime.now())
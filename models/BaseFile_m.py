from datetime import datetime
from typing import Optional
import uuid

from sqlalchemy import Column, DateTime
from sqlalchemy.dialects import postgresql as psql

from pydantic import BaseModel,Field
class ModelBase(BaseModel):
    """
    Base class for database models.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=datetime.utcnow))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True),
                                 onupdate=datetime.utcnow, default=datetime.utcnow))
import uuid as uuid_pkg


class UUIDModelBase(ModelBase):
    """
    Base class for UUID-based models.
    """
    uuid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )



class Table_excel(BaseModel):
    tables: str

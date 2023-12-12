from sqlalchemy import (
    Column,
    Date,
    ForeignKey,
    Integer,
    Numeric,
    String,
    DateTime,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import uuid,datetime
from sqlalchemy.dialects.postgresql import UUID
from typing import Optional,Annotated
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy.sql import func

Base = declarative_base()


# create_at = Column(DateTime(timezone=True), server_default=func.now())
# update_at = Column(DateTime(timezone=True), onupdate=func.now())
class BaseFail(Base):
    __tablename__ = 'BaseFile_t'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    create_at =  Column(DateTime(timezone=True), server_default=func.now())
    # create_at =  Mapped[create_at]
    # update_at =  Mapped[update_at]

from  database import engine
from  tables_New_Create import Base
Base.metadata.create_all(engine)
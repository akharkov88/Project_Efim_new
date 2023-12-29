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
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    # email = Column(String, unique=True)
    username = Column(String, unique=True)
    password_hash = Column(String)
#
#
#
class TaskForm(Base):
    __tablename__ = 'TechTaskForm'

    id = Column(Integer, primary_key=True)
    NameTechTask = Column(String, unique=True) # Наименование обекта
    TechTaskClient = Column(String) # Наименование заказчика
    TechTaskProject = Column(String) # Проект/чертеж
    TechTaskPPR = Column(String) # Проект/чертеж
    TechTaskOverhead = Column(String) # Накладные расходы
    TechTaskDateKP = Column(String)#Column(Date) #  Срок подготовки КП
    TechTaskDateEndWork = Column(String) #  Срок выполнение работ
    TechTaskPrice = Column(String) #  Условия оплаты
    TechTaskLeaderKP = Column(String) #  Отвественный
    user_name = Column(String, ForeignKey('users.username'), index=True)
#
# # create_at = Column(DateTime(timezone=True), server_default=func.now())
# # update_at = Column(DateTime(timezone=True), onupdate=func.now())
# class BaseFail(Base):
#     __tablename__ = 'BaseFile_t'
#     id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     name = Column(String, nullable=False)
#     create_at =  Column(DateTime(timezone=True), server_default=func.now())
#     user_name = Column(String, ForeignKey('users.username'), index=True)

    # create_at =  Mapped[create_at]
    # update_at =  Mapped[update_at]

class PTO_Value(Base):
    __tablename__ = 'PTO_Value'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    NameTechTask_key = Column(String, ForeignKey('TechTaskForm.NameTechTask'), index=True)
    user_name = Column(String, ForeignKey('users.username'), index=True)
    value_table = Column(String, nullable=False)
    create_at = Column(DateTime(timezone=True), server_default=func.now())
    update_at = Column(DateTime(timezone=True), server_default=func.now())

from  database import engine
from  tables_New_Create import Base
Base.metadata.create_all(engine)
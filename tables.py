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
import uuid
from sqlalchemy.dialects.postgresql import UUID
from typing import Optional,Annotated
Base = declarative_base()
from sqlalchemy.orm import Mapped,mapped_column
import datetime
from sqlalchemy.sql import func


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    # email = Column(String, unique=True)
    username = Column(String, unique=True)
    password_hash = Column(String)


class Operation(Base):
    __tablename__ = 'operations'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), index=True)
    date = Column(Date)
    kind = Column(String)
    amount = Column(Numeric(10, 2))
    description = Column(String, nullable=True)

    user = relationship('User', backref='operations')



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
    # date = Column(Date)
    # kind = Column(String)
    # amount = Column(Numeric(10, 2))
    # description = Column(String, nullable=True)
    #
    # user = relationship('User', backref='operations')


    # from  database import engine
    # from  tables import Base
    # Base.metadata.create_all(engine)

create_at = Column(DateTime(timezone=True), server_default=func.now())
update_at = Column(DateTime(timezone=True), onupdate=func.now())
class BaseFile(Base):
    __tablename__ = 'BaseFile_t'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    create_at =  Column(DateTime(timezone=True), server_default=func.now())
    # create_at =  Mapped[create_at]
    # update_at =  Mapped[update_at]


    # from  database import engine
    # from  tables import Base
    # Base.metadata.create_all(engine)



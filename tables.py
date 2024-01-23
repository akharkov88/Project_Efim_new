from sqlalchemy import (
    Column,
    Date,
    ForeignKey,
    Integer,
    Numeric,
    String,
    DateTime,
    UniqueConstraint,
    Enum,
    Boolean,
)
from sqlalchemy.dialects.postgresql import ENUM as PgEnum
# from sqlalchemy.dialects import postgresql
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
    roles = Column(String)


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
    user_name = Column(String, ForeignKey('users.username'), index=True)

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
    user_name = Column(String, ForeignKey('users.username'), index=True)

class PTO_Value(Base):
    __tablename__ = 'PTO_Value'
    NameTechTask_key = Column(String, ForeignKey('TechTaskForm.NameTechTask'), index=True, primary_key=True)
    user_name = Column(String, ForeignKey('users.username'), index=True)
    value_table = Column(String, nullable=False)
    create_at = Column(DateTime(timezone=True), server_default=func.now())



class Suggest(Base):
    __tablename__ = 'Suggest_Value'
    id = Column(Integer, primary_key=True)
    customer_id = Column(String)
    value_table = Column(String)
    create_at = Column(DateTime(timezone=True), server_default=func.now())
    user_name = Column(String, ForeignKey('users.username'), index=True)

    __table_args__ = (
        UniqueConstraint('customer_id', 'value_table', name='uix_customer_id_value_table'),
    )




class ListUserTask(Base):
    __tablename__ = 'List_User_Task'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_executor= Column(String)
    result= Column(String)
    status  = Column(String)
    target_date= Column(Date)
    create_at= Column(DateTime(timezone=True), server_default=func.now())
    update_at= Column(DateTime(timezone=True), onupdate=func.now())
    user_create = Column(String, ForeignKey('users.username'), index=True)
    notification_holder = Column(Boolean)
    notification_executor = Column(Boolean)
    priority = Column(String)


class UserPfofile(Base):
    __tablename__ = 'UserPfofile'
    username = Column(String, ForeignKey('users.username'), index=True, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    telegram = Column(String)
    mobile = Column(String)
    worker_tel = Column(String)
    email = Column(String)
    adress = Column(String)
    office = Column(String)


    # from  database import engine
    # from  tables import Base
    # Base.metadata.create_all(engine)



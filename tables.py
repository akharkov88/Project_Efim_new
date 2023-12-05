from sqlalchemy import (
    Column,
    Date,
    ForeignKey,
    Integer,
    Numeric,
    String,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


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
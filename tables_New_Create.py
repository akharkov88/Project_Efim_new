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

from  database import engine
from  tables_New_Create import Base
Base.metadata.create_all(engine)
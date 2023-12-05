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
    __tablename__ = 'TaskForm'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    # date = Column(Date)
    # kind = Column(String)
    # amount = Column(Numeric(10, 2))
    # description = Column(String, nullable=True)
    #
    # user = relationship('User', backref='operations')


from  database import engine
from  tables_New_Create import Base
Base.metadata.create_all(engine)
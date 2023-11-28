import datetime
import enum

from sqlalchemy import Table,Column,Integer,String,MetaData,ForeignKey
from sqlalchemy.orm import Mapped,mapped_column
# from Alchemy import Base22
from alchemy import Base,text,str256
from typing import Optional,Annotated


metadata_obj=MetaData()

workers_table=Table(
    "workers",
    metadata_obj,
    Column("id",Integer,primary_key=True),
    Column ("username",String)
)
intpk=Annotated[int,mapped_column(primary_key=True)]
create_at=Annotated[datetime.datetime,mapped_column(server_default=text("TIMEZONE(utc,now())"))]
update_at=Annotated[datetime.datetime,mapped_column(server_default=text("TIMEZONE(utc,now())"),onupdate=datetime.datetime.utcnow)]

class WorkersORM(Base):
    __tablename__ = 'workers'

    id: Mapped[intpk]
    username: Mapped[str]


class Workload(enum.Enum):
    partime= "partime"
    fulltime= "fulltime"

class ResumeORM(Base):
    __tablename__ = 'resume'

    id: Mapped[intpk]
    title: Mapped[str256]
    competation: Mapped[Optional[int]] #Optional- означает может быть пустым
    Workload: Mapped[Workload] #Optional- означает может быть пустым
    worker_id: Mapped[int]=mapped_column(ForeignKey("workers.id", ondelete="CASCADE"))
    create_at: Mapped[create_at]
    update_at: Mapped[update_at]


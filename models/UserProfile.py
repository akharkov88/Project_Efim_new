from pydantic import BaseModel
from datetime import datetime, timezone,date
from enum import Enum

class progressEnum(str, Enum):
    WAITING_FOR_WORKER = 'Назначена'
    IN_PROGRESS = 'В Работе'
    completed = 'Выполнено'
    fault = 'Отказ выполнять'

class ModelUserTask(BaseModel):
    name: str
    user_create: str
    user_executor: str
    progress: str
    status : str
    target_date: date

class ModelUserPfofile(BaseModel):
    first_name: str
    last_name: str
    telegram: str
    work_tel: str
    email: str
    adress: str
    office: str


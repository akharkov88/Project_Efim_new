from pydantic import BaseModel
from datetime import datetime, timezone,date
from enum import Enum

class statusEnum(str, Enum):
    WAITING_FOR_WORKER = 'Назначена'
    IN_PROGRESS = 'В Работе'
    completed = 'Выполнено'
    fault = 'Отказ выполнять'

class priorityEnum(str, Enum):
    low = 'Не важно'
    normal = 'Нормально'
    danger = 'Важно'

class ModelUserTask(BaseModel):
    name: str
    user_create: str
    user_executor: str
    status: statusEnum
    result : str
    target_date: date
    notification_holder: bool
    notification_executor: bool
    priority: priorityEnum

class ModelUserPfofile(BaseModel):
    first_name: str
    last_name: str
    telegram: str
    mobile: str
    worker_tel: str
    email: str
    adress: str
    office: str


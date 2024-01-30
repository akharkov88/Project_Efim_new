from pydantic import BaseModel
from pydantic.main import ModelMetaclass
from datetime import datetime, timezone,date
from enum import Enum
from typing import Optional
class statusEnum(str, Enum):
    WAITING_FOR_WORKER = 'Назначена'
    IN_PROGRESS = 'В Работе'
    completed = 'Выполнено'
    fault = 'Отказ выполнять'

class priorityEnum(str, Enum):
    low = 'Не важно'
    normal = 'Нормально'
    danger = 'Важно'
class ModelUserTaskID(BaseModel):
    id: int
class ModelUserTaskUpdate(BaseModel):
    status: statusEnum
    result : str
    notification_holder: bool
    notification_executor: bool

class ModelUserTask(ModelUserTaskID):
    name: str
    user_create: str
    user_executor: str
    status: statusEnum
    result : str
    target_date: date
    notification_holder: bool
    notification_executor: bool
    priority: priorityEnum


class AllOptional(ModelMetaclass):
    def __new__(self, name, bases, namespaces, **kwargs):
        annotations = namespaces.get('__annotations__', {})
        for base in bases:
            annotations.update(base.__annotations__)
        for field in annotations:
            if not field.startswith('__'):
                annotations[field] = Optional[annotations[field]]
        namespaces['__annotations__'] = annotations
        return super().__new__(self, name, bases, namespaces, **kwargs)

class UpdatedItem(ModelUserTask, metaclass=AllOptional):
    pass

class ModelUserPfofile(BaseModel):
    first_name: str
    last_name: str
    telegram: str
    mobile: str
    worker_tel: str
    email: str
    adress: str
    office: str


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
    reversed = 'Возврат в работу'

class priorityEnum(str, Enum):
    low = 'Не важно'
    normal = 'Нормально'
    danger = 'Важно'
class event(str, Enum):
    add = 'add'
    delete = 'del'
class ModelUserTaskID(BaseModel):
    id: int
class ModelUserTaskEventControl(ModelUserTaskID):
    event: event
class ModelUserTaskUpdate(BaseModel):
    status: statusEnum
    result : str
    notification_holder: bool
    notification_executor: bool

class ModelUserTask(BaseModel):
    name: str
    user_executor: str
    status: statusEnum
    result : str
    target_date: date
    notification_holder: bool
    notification_executor: bool
    priority: priorityEnum
    connection: str


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
    department: str


class ModelUserPfofile_my_username(ModelUserPfofile):
    my_username: str

class eventDepartment(str, Enum):
    add = 'add'
    dell = 'del'
class ModelgetDepartment(BaseModel):
    value: str
    event: eventDepartment


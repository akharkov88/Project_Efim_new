from pydantic import BaseModel


class BaseTask(BaseModel):
    id: int
    class Config:
        orm_mode = True

class UserTask(BaseTask):
    username: str
class TaskCreate(BaseTask):
    pass

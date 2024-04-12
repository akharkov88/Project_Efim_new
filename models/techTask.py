from pydantic import BaseModel


class BaseTechTaskPTO(BaseModel):
    NameTechTask_key: str

class TechTaskPTO(BaseTechTaskPTO):
    value_table: str
    description: str

class TechTaskPTO_key(BaseTechTaskPTO):
    sum: int
class TechTaskPTO_id(BaseModel):
    id: int

class WorkingNameTechTask(BaseModel):
    NameTechTask: str
    state: bool


class WorkingAll(WorkingNameTechTask):
    update_at: str
    username: str

class Response_WorkingNameTechTask(BaseModel):
    state: bool
    user: str



# class BaseTechTaskPTO(TechTaskPTO):
#     id: int
#     class Config:
#         orm_mode = True


# class TaskCreate(BaseTechTaskPTO):
#     pass

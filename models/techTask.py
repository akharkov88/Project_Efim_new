from pydantic import BaseModel


class BaseTechTaskPTO(BaseModel):
    NameTechTask_key: str

class TechTaskPTO(BaseTechTaskPTO):
    value_table: str

# class BaseTechTaskPTO(TechTaskPTO):
#     id: int
#     class Config:
#         orm_mode = True


# class TaskCreate(BaseTechTaskPTO):
#     pass

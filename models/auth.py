from pydantic import BaseModel


class BaseUser(BaseModel):
    # email: str
    username: str

class UserRoles(BaseUser):
    roles: str

class UserCreate(UserRoles):
    password: str



class User(BaseUser):
    id: int
    roles: str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'

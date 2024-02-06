from pydantic import BaseModel


class BaseTelegram(BaseModel):
    User: str
    Value: str

class BaseTelegram_group(BaseModel):
    Value: str

class BaseUserTelegram(BaseModel):
    name_user_telegram: str
    id_telegram: str

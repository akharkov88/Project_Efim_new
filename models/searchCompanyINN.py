from pydantic import BaseModel
from pydantic.main import ModelMetaclass
from datetime import datetime, timezone,date
from enum import Enum
from typing import Optional

class ModelSearchCompanyINN(BaseModel):
    q: int
    filter: str

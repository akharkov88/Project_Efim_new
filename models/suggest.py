from pydantic import BaseModel


class BaseSuggest(BaseModel):
    customer_id: str

class SuggestM(BaseSuggest):
    value_table: str

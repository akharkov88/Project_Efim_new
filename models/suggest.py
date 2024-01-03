from pydantic import BaseModel


class BaseSuggest(BaseModel):
    customer_id: str

class CountSuggest(BaseSuggest):
    count: int

class SuggestM(BaseSuggest):
    value_table: str

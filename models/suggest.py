from pydantic import BaseModel


class BaseSuggest(BaseModel):
    customer_id: str

class CountSuggest(BaseSuggest):
    search: str
    count: int

class SuggestM(BaseSuggest):
    value_table: str

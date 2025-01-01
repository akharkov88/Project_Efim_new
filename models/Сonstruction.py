from pydantic import BaseModel




class ModelConstruction(BaseModel):
    idCompanyStructure:int
    Наименнование:str
    Местоположение :str
    ВидОбъекта:str
    Описание:str

class ModelConstructionID(BaseModel):
    id:int
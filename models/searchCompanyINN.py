from pydantic import BaseModel
from pydantic.main import ModelMetaclass
from datetime import datetime, timezone,date
from enum import Enum
from typing import Optional

class ModelSearchCompanyINN(BaseModel):
    q: int
    filter: str


class CompanyStructure(BaseModel):
    INN: str #ИНН
    OGRN: str #ОГРН
    NameAbbreviatedLegal: str #НаимСокрЮЛ
    NameFullLegal: str #НаимПолнЮЛ
    DateOGRN: str  #ДатаОГРН
    Status: str #Статус
    FullAddress: str #АдресПолн
    MainTypeActivity: str #ОснВидДеят
    WhereFound: str #ГдеНайдено


class CompanyStructure1(BaseModel):
    ИНН: str
    ОГРН: str
    НаимСокрЮЛ: str
    НаимПолнЮЛ: str
    ДатаОГРН: str
    Статус: str
    АдресПолн: str
    ОснВидДеят: str
    ГдеНайдено: str

class CompanyStructureLegal(BaseModel):
    ЮЛ:CompanyStructure1

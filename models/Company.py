from pydantic import BaseModel
from pydantic.main import ModelMetaclass
from datetime import datetime, timezone,date
from enum import Enum
from typing import Optional
# from __future__ import annotations

from typing import Any, Dict, List, Optional

class ModelCompany(BaseModel):
    inn: int
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


class GetCompanyStructureLegal(BaseModel):
    id: int

class GetCompanyStructureLegal(BaseModel):
    id: int

class test(BaseModel):
    page: int
    size: int

class GetPainting(BaseModel):
    test:test




#
#
# class Статус(BaseModel):
#     Код: str
#     Наим: str
#
#
# class Регион(BaseModel):
#     Код: str
#     Наим: str
#
#
# class ЮрАдрес(BaseModel):
#     НасПункт: str
#     АдресРФ: str
#     ИдГАР: Any
#     Недост: bool
#
#
# class ОКВЭД(BaseModel):
#     Код: str
#     Наим: str
#     Версия: str
#
#
# class ОКВЭДДопItem(BaseModel):
#     Код: str
#     Наим: str
#     Версия: str
#
#
# class ОКОПФ(BaseModel):
#     Код: str
#     Наим: str
#
#
# class ОКФС(BaseModel):
#     Код: str
#     Наим: str
#
#
# class ОКОГУ(BaseModel):
#     Код: str
#     Наим: str
#
#
# class ОКАТО(BaseModel):
#     Код: str
#     Наим: str
#
#
# class ОКТМО(BaseModel):
#     Код: str
#     Наим: str
#
#
# class РегФНС(BaseModel):
#     КодОрг: str
#     НаимОрг: str
#     АдресОрг: str
#
#
# class ТекФНС(BaseModel):
#     КодОрг: str
#     НаимОрг: str
#     ДатаПостУч: str
#
#
# class РегПФР(BaseModel):
#     ДатаРег: str
#     РегНомер: str
#     КодОрг: str
#     НаимОрг: str
#
#
# class РегФСС(BaseModel):
#     ДатаРег: str
#     РегНомер: str
#     КодОрг: str
#     НаимОрг: str
#
#
# class УстКап(BaseModel):
#     Тип: str
#     Сумма: int
#
#
# class РуководItem(BaseModel):
#     ФИО: str
#     ИНН: str
#     ВидДолжн: str
#     НаимДолжн: str
#     Недост: bool
#     МассРуковод: bool
#     ДисквЛицо: bool
#     СвязРуковод: List
#     СвязУчред: List
#     ДатаЗаписи: str
#
#
# class Доля(BaseModel):
#     Номинал: int
#     Процент: int
#
#
# class ФЛItem(BaseModel):
#     ФИО: str
#     ИНН: str
#     Недост: bool
#     МассУчред: bool
#     Доля: Доля
#     СвязРуковод: List[str]
#     СвязУчред: List[str]
#     ДатаЗаписи: str
#
#
# class Учред(BaseModel):
#     ФЛ: List[ФЛItem]
#     РосОрг: List
#     ИнОрг: List
#     ПИФ: List
#     РФ: List
#
#
# class Контакты(BaseModel):
#     Тел: List[str]
#     Емэйл: List
#     ВебСайт: Any
#
#
# class СведУплItem(BaseModel):
#     Наим: str
#     Сумма: float
#
#
# class Налоги(BaseModel):
#     ОсобРежим: List
#     СведУпл: List[СведУплItem]
#     СумУпл: str
#     СведУплГод: str
#     СумНедоим: Any
#
#
# class РМСП(BaseModel):
#     Кат: str
#     ДатаВкл: str
#
#
# class ПоддержМСПItem(BaseModel):
#     Дата: str
#     Тип: str
#     Форма: str
#     НаимОрг: str
#     ИНН: str
#     Размер: str
#     Наруш: bool
#
#
# class Data(BaseModel):
#     ОГРН: str
#     ИНН: str
#     КПП: str
#     ОКПО: str
#     ДатаРег: str
#     ДатаОГРН: str
#     НаимСокр: str
#     НаимАнгл: Any
#     НаимПолн: str
#     Статус: Статус
#     Регион: Регион
#     ЮрАдрес: ЮрАдрес
#     ОКВЭД: ОКВЭД
#     ОКВЭДДоп: List[ОКВЭДДопItem]
#     ОКОПФ: ОКОПФ
#     ОКФС: ОКФС
#     ОКОГУ: ОКОГУ
#     ОКАТО: ОКАТО
#     ОКТМО: ОКТМО
#     РегФНС: РегФНС
#     ТекФНС: ТекФНС
#     РегПФР: РегПФР
#     РегФСС: РегФСС
#     УстКап: УстКап
#     УпрОрг: Dict[str, Any]
#     Руковод: List[РуководItem]
#     Учред: Учред
#     СвязУпрОрг: List
#     СвязУчред: List
#     ДержРеестрАО: Dict[str, Any]
#     Лиценз: List
#     ТоварЗнак: List
#     Подразд: Dict[str, Any]
#     Правопредш: List
#     Правопреем: List
#     ДатаВып: str
#     Контакты: Контакты
#     Налоги: Налоги
#     РМСП: РМСП
#     ПоддержМСП: List[ПоддержМСПItem]
#     СЧР: int
#     СЧРГод: str
#     ЕФРСБ: List
#     НедобПост: bool
#     ДисквЛица: bool
#     МассРуковод: bool
#     МассУчред: bool
#     НелегалФин: bool
#     Санкции: bool
#
#
# class Meta(BaseModel):
#     status: str
#     today_request_count: int
#     balance: int
#
#
# class Model(BaseModel):
#     data: Data
#     meta: Meta


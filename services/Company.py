from datetime import (
    datetime,
    timedelta,
)
import ast
import math
from pydantic import BaseModel,Field
from sqlalchemy import select
from pandas.core.computation.pytables import Constant
from pytz import timezone
import traceback
from typing import (
    List,
    Optional,
)

from fastapi import (
    Depends,
    HTTPException,
    status,
)
import dateutil.parser
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_, not_
from services.Telegram import ClassTelegram

import models
import json
import tables
from services.auth import get_session
from fastapi.encoders import jsonable_encoder
from sqlalchemy.dialects.postgresql import Any
import asyncio
import requests
import Constants

class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


class CompanyServicesClass:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session


    def services_SearchCompanyINN(self, param_search: models.Company) -> str:
        # response = await asyncio.get_event_loop().run_in_executor(None, requests.get, "https://api-fns.ru/api/search",
        #                                                           data={"q":"5259107913","key":"d4a0ff06fad2f9491613657c091753fc143c2ab4"})
        # return response
        params = {
            'q': param_search.inn,
            'filter': param_search.filter,
            'key': Constants.key
        }

        # r = requests.get('https://api-fns.ru/api/search', params=params)
        r = requests.get(f'https://api.ofdata.ru/v2/company?key={Constants.keyOfdata}&inn={param_search.inn}')
        #offline https://ofdata.ru/open-data
        return r.text
    # response = asyncio.run(services_Company(param_search))

    def services_saveCompanyINN(self, param_save: models.CompanyStructure) -> str:
        try:
            operation = tables.CompanyStructure(**dict(dict(param_save)["ЮЛ"]))
            self.session.add(operation)
            self.session.flush()
            self.session.refresh(operation)
            rez=jsonable_encoder(operation)
            self.session.commit()
            if not operation:
                return HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ошибка повторите еще раз")
            return json.dumps(rez)

        except:
            print(traceback.format_exc())
            raise HTTPException(status.HTTP_409_CONFLICT, detail="Организация с стаким наименованием уже существует")

    def services_getCompany(self,id_company:int,page:int, size:int) -> str:
        try:
            q = (
                self.session
                .query(tables.CompanyStructure))

            if id_company!=None:
                q=q.filter(tables.CompanyStructure.id == id_company)
            operation=q.all()
            if id_company==None and page!=None and size!=None:

                offset_min = page * size
                offset_max = (page + 1) * size

                operation = operation[offset_min:offset_max] + [
                    {
                        "page": page,
                        "size": size,
                        "total": math.ceil(len(operation) / size) - 1,
                    }
                ]

            return operation

        except:
            print(traceback.format_exc())
            raise HTTPException(status.HTTP_409_CONFLICT, detail="Организация с стаким наименованием уже существует")


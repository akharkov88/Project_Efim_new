from datetime import (
    datetime,
    timedelta,
)
import ast

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


class SearchCompanyINNServicesClass:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session


    def services_searchCompanyINN(self, param_search: models.searchCompanyINN) -> str:
        # response = await asyncio.get_event_loop().run_in_executor(None, requests.get, "https://api-fns.ru/api/search",
        #                                                           data={"q":"5259107913","key":"d4a0ff06fad2f9491613657c091753fc143c2ab4"})
        # return response
        params = {
            'q': param_search.q,
            'filter': param_search.filter,
            'key': Constants.key
        }

        r = requests.get('https://api-fns.ru/api/search', params=params)
        return r.text
    # response = asyncio.run(services_searchCompanyINN(param_search))
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


class СonstructionServicesClass:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session


    def updateConstruction(self,id: models.ModelConstructionID, param_save: models.ModelConstruction) -> str:
        operation = (
            self.session
            .query(tables.Сonstruction)
            .filter(
                tables.Сonstruction.id == id.id
            )
            .first()
        )

        if not operation:
            return HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Отсутствует ID")

        try:

            self.session.query(tables.Сonstruction).filter(tables.Сonstruction.id == id.id).update(dict(param_save))
            self.session.commit()
            operation = (
                self.session
                .query(tables.Сonstruction)
                .filter(
                    tables.Сonstruction.id == id.id
                )
                .first()
            )

            if not operation:
                return HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ошибка повторите еще раз")
            return jsonable_encoder(operation)

        except:
            print(traceback.format_exc())
            raise HTTPException(status.HTTP_409_CONFLICT, detail="Объект с стаким наименованием уже существует")

    def services_addConstruction(self, param_save: models.ModelConstructionPost) -> str:
        try:
            operation = tables.Сonstruction(**dict(param_save.data))
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
            raise HTTPException(status.HTTP_409_CONFLICT, detail="Объект с стаким наименованием уже существует")

    def services_getConstruction(self,id_construction:int,page:int, size:int) -> str|List[dict]:
        try:
            q = (
                self.session
                .query(tables.Сonstruction))

            if id_construction!=None:
                q=q.filter(tables.Сonstruction.id == id_construction)
            operation=q.all()
            if id_construction==None and page!=None and size!=None:

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


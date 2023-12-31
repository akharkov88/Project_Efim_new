import datetime
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
from sqlalchemy.orm import Session

import models
import tables
from services.auth import  get_session
from fastapi.encoders import jsonable_encoder

class TechTaskServices:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def createTechTaskPTO_S(self,TechTaskDATA: models.TechTaskPTO ,user: tables.User,) -> tables.PTO_Value:
        try:


            operation = tables.PTO_Value(
                value_table=TechTaskDATA.value_table,
                NameTechTask_key=TechTaskDATA.NameTechTask_key,
                user_name=user.username,
            )
            self.session.add(operation)
            self.session.commit()
            operation = (
                self.session
                .query(tables.PTO_Value)
                .filter(
                    tables.PTO_Value.NameTechTask_key == TechTaskDATA.NameTechTask_key
                )
                .first()
            )
            if not operation:
                raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ошибка повторите еще раз")
            # return jsonable_encoder(operation)
            return jsonable_encoder(operation)

        except:
            print(traceback.format_exc())
            raise HTTPException(status.HTTP_409_CONFLICT, detail="Error no name NameTechTask_key")
            # raise JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'message': "Уже существует запись"})


        # return "operation"
    def getTechTaskPTO_S(self,TechTaskDATA: models.BaseTechTaskPTO ,user: tables.User,) -> tables.PTO_Value:
        try:
            operation = (
                self.session
                .query(tables.PTO_Value)
                .filter(
                    tables.PTO_Value.NameTechTask_key == TechTaskDATA.NameTechTask_key
                )
                .order_by(
                    tables.PTO_Value.create_at.desc()
                )
                .first()
            )
            if not operation:
                raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ошибка повторите еще раз")
            # return jsonable_encoder(operation)
            return jsonable_encoder(operation)
        except:
            print(traceback.format_exc())
            raise HTTPException(status.HTTP_409_CONFLICT, detail="Error no name NameTechTask_key")
            # raise JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'message': "Уже существует запись"})


        # return "operation"
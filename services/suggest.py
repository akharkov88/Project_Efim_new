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

class SuggestServices:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_suggest(self,TechTaskDATA: models.BaseSuggest ,user: tables.User,) -> tables.Suggest:
        try:

            operation = (
                self.session
                .query(tables.Suggest)
                .filter(
                    tables.Suggest.customer_id == TechTaskDATA.customer_id,
                )
                .all()
            )
            if not operation:
                raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ошибка повторите еще раз")
            # return jsonable_encoder(operation)
            return jsonable_encoder(operation)

        except:
            print(traceback.format_exc())
            raise HTTPException(status.HTTP_409_CONFLICT, detail="Error")
            # raise JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'message': "Уже существует запись"})

    def set_suggest(self,TechTaskDATA: models.SuggestM ,user: tables.User,) -> tables.Suggest:
        try:


            operation = tables.Suggest(
                value_table=TechTaskDATA.value_table,
                customer_id=TechTaskDATA.customer_id,
                user_name=user.username,
            )
            self.session.add(operation)
            self.session.commit()
            operation = (
                self.session
                .query(tables.Suggest)
                .filter(
                    tables.Suggest.customer_id == TechTaskDATA.customer_id,
                )
                .all()
            )
            if not operation:
                raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ошибка повторите еще раз")
            # return jsonable_encoder(operation)
            return jsonable_encoder(operation)

        except:
            print(traceback.format_exc())
            raise HTTPException(status.HTTP_409_CONFLICT, detail="Duplicate key")
            # raise JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'message': "Уже существует запись"})
    def delete_suggest(self,TechTaskDATA: models.SuggestM ,user: tables.User,) -> tables.Suggest:
        try:

            self.session.query(tables.Suggest).filter(tables.Suggest.customer_id == TechTaskDATA.customer_id,tables.Suggest.value_table == TechTaskDATA.value_table).delete()
            self.session.commit()

            # operation = tables.Suggest(
            #     value_table=TechTaskDATA.value_table,
            #     customer_id=TechTaskDATA.customer_id,
            #     user_name=user.username,
            # )
            # self.session.add(operation)
            # self.session.commit()
            operation = (
                self.session
                .query(tables.Suggest)
                .filter(
                    tables.Suggest.customer_id == TechTaskDATA.customer_id,
                )
                .all()
            )
            if not operation:
                raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ошибка повторите еще раз")
            # return jsonable_encoder(operation)
            return jsonable_encoder(operation)

        except:
            print(traceback.format_exc())
            raise HTTPException(status.HTTP_409_CONFLICT, detail="Duplicate key")
            # raise JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'message': "Уже существует запись"})

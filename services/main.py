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
# from database import get_current_user
#
# print(get_current_user)
class TaskServices:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def createTask_S(self,username: models.UserTask) -> tables.TaskForm:
        try:
            operation = tables.TaskForm(
                username=username,
            )
            self.session.add(operation)
            self.session.commit()
            operation = (
                self.session
                .query(tables.TaskForm)
                .filter(
                    tables.TaskForm.username == username
                )
                .first()
            )
            if not operation:
                raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ошибка повторите еще раз")
            # return jsonable_encoder(operation)
            return jsonable_encoder(operation)
        except:
            print(traceback.format_exc())
            raise HTTPException(status.HTTP_409_CONFLICT, detail="Запись с таким именем уже существует запись")
            # raise JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'message': "Уже существует запись"})


        # return "operation"
    def getAllTask_S(self) -> tables.TaskForm:
        try:
            operation = (
                self.session
                .query(tables.TaskForm)
                .all()
            )
            # if not operation:
            #     raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ошибка повторите еще раз")
            # return jsonable_encoder(operation)
            return jsonable_encoder(operation)
        except:
            print(traceback.format_exc())
            raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR)
            # raise JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'message': "Уже существует запись"})


        # return "operation"

        getAllTask_S
    def getTechTaskUsername_S(self,username: models.UserTask) -> tables.TaskForm:
        try:
            operation = (
                self.session
                .query(tables.TaskForm)
                .filter(
                    tables.TaskForm.username == username
                )
                .first()
            )
            if not operation:
                raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Нет такого username")
            return jsonable_encoder(operation)
        except:
            print(traceback.format_exc())
            raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR)
            # raise JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'message': "Уже существует запись"})


        # return "operation"

        getAllTask_S
    #
    # def update(
    #     self,
    #     user_id: int,
    #     operation_id: int,
    #     operation_data: models.OperationUpdate,
    # ) -> tables.Operation:
    #     operation = self._get(user_id, operation_id)
    #     for field, value in operation_data:
    #         setattr(operation, field, value)
    #     self.session.commit()
    #     return operation
    #
    # def delete(
    #     self,
    #     user_id: int,
    #     operation_id: int,
    # ):
    #     operation = self._get(user_id, operation_id)
    #     self.session.delete(operation)
    #     self.session.commit()


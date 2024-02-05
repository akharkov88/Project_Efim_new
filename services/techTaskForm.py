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
import os
import pathlib
from services.auth import  get_session
from fastapi.encoders import jsonable_encoder
# from database import get_current_user
#
# print(get_current_user)
class techTaskFormServices:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def update_value(self, TechTaskDATA: models.UserTask) -> tables.TaskForm:
        try:
            # operation = tables.TaskForm(
            #     NameTechTask=TechTaskDATA.NameTechTask,
            #     TechTaskClient=TechTaskDATA.TechTaskClient,
            #     TechTaskProject=TechTaskDATA.TechTaskProject,
            #     TechTaskPPR=TechTaskDATA.TechTaskPPR,
            #     TechTaskOverhead=TechTaskDATA.TechTaskOverhead,
            #     TechTaskDateKP=TechTaskDATA.TechTaskDateKP,
            #     TechTaskDateEndWork=TechTaskDATA.TechTaskDateEndWork,
            #     TechTaskPrice=TechTaskDATA.TechTaskPrice,
            #     TechTaskLeaderKP=TechTaskDATA.TechTaskLeaderKP,
            # )

            # existing_row = self.session.query(tables.TaskForm).filter(tables.TaskForm.NameTechTask == TechTaskDATA.NameTechTask).first()
            # existing_row.column1 = 'new_value1'
            # existing_row.column2 = 'new_value2'
            # existing_row.TechTaskClient = TechTaskDATA.TechTaskClient,
            # self.session.commit()


            self.session.query(tables.TaskForm).filter(tables.TaskForm.NameTechTask == TechTaskDATA.NameTechTask).update(dict(TechTaskDATA))
            self.session.commit()
            operation = (
                self.session
                .query(tables.TaskForm)
                .filter(
                    tables.TaskForm.NameTechTask == TechTaskDATA.NameTechTask
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

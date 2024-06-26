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
import pytz
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
                description=TechTaskDATA.description,
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
            value_return=jsonable_encoder(operation)
            value_return["create_at"]=datetime.datetime.fromisoformat(value_return["create_at"]).strftime("%Y-%m-%d %H:%M:%S")
            return value_return
        except:
            print(traceback.format_exc())
            raise HTTPException(status.HTTP_409_CONFLICT, detail="Error no name NameTechTask_key")
            # raise JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'message': "Уже существует запись"})


        # return "operation"      # return "operation"


    def getTechTaskPTO_key_S(self,TechTaskDATA: models.BaseTechTaskPTO ,user: tables.User,) -> tables.PTO_Value:
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
                .all()
            )
            if not operation:
                raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ошибка повторите еще раз")
            # return jsonable_encoder(operation)

            value_return=jsonable_encoder(operation)

            for i,val in enumerate(value_return):
                value_return[i]["create_at"]=datetime.datetime.fromisoformat(value_return[i]["create_at"]).strftime("%Y-%m-%d %H:%M:%S")

            return value_return[:TechTaskDATA.sum]
        except:
            print(traceback.format_exc())
            raise HTTPException(status.HTTP_409_CONFLICT, detail="Error no name NameTechTask_key")
            # raise JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'message': "Уже существует запись"})


        # return "operation"
    def getTechTaskPTO_id_S(self,TechTaskDATA: models.BaseTechTaskPTO ,user: tables.User,) -> tables.PTO_Value:
        try:
            operation = (
                self.session
                .query(tables.PTO_Value)
                .filter(tables.PTO_Value.id == TechTaskDATA.id)

                .order_by(
                    tables.PTO_Value.create_at.desc()
                )
                .first()
            )
            if not operation:
                raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ошибка повторите еще раз")
            # return jsonable_encoder(operation)
            value_return=jsonable_encoder(operation)
            value_return["create_at"]=datetime.datetime.fromisoformat(value_return["create_at"]).strftime("%Y-%m-%d %H:%M:%S")
            return value_return
        except:
            print(traceback.format_exc())
            raise HTTPException(status.HTTP_409_CONFLICT, detail="Error no name NameTechTask_key")
            # raise JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'message': "Уже существует запись"})


        # return "operation"


    def SetWorkingTable_NameTechTask(self,NameTechTask: models.WorkingNameTechTask,user: tables.User):


        try:
            operation_ID_NameTechTask = (
                self.session
                .query(tables.PTO_Value)
                .filter(
                    tables.PTO_Value.NameTechTask_key == NameTechTask.NameTechTask
                )
                .order_by(
                    tables.PTO_Value.create_at.desc()
                )
                .first()
            )
            id_actual_table=jsonable_encoder(operation_ID_NameTechTask)["id"]
            operation = (
                self.session
                .query(tables.WorkingTable)
                .filter(
                    tables.WorkingTable.NameTechTask == NameTechTask.NameTechTask
                )

                .first()
            )
            if not operation:
                operation = tables.WorkingTable(
                    NameTechTask=NameTechTask.NameTechTask,
                    username=user.username,
                    state=NameTechTask.state,
                )
                self.session.add(operation)
                self.session.commit()
                operation = (
                    self.session
                    .query(tables.WorkingTable)
                    .filter(
                        tables.WorkingTable.NameTechTask == NameTechTask.NameTechTask
                    )
                    .first()
                )
                if not operation:
                    raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ошибка повторите еще раз")
                else:
                   return {"state":NameTechTask.state,"user":"","id_actual_table":id_actual_table}
            utc = pytz.UTC
            if jsonable_encoder(operation)["username"]==user.username or (datetime.datetime.fromisoformat(jsonable_encoder(operation)["update_at"])+datetime.timedelta(minutes=5))<utc.localize(datetime.datetime.utcnow()):

                self.session.query(tables.WorkingTable).filter(
                    tables.WorkingTable.NameTechTask == NameTechTask.NameTechTask).update({"username": user.username,"state":NameTechTask.state})
                self.session.commit()
                operation = (
                    self.session
                    .query(tables.WorkingTable)
                    .filter(
                        tables.WorkingTable.NameTechTask == NameTechTask.NameTechTask
                    )
                    .first()
                )
                if not operation:
                    raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ошибка повторите еще раз")
                return {"state": NameTechTask.state, "user": "","id_actual_table":id_actual_table}

            else:
                return {"state":False,"user":jsonable_encoder(operation)["username"],"id_actual_table":id_actual_table}
            #
            # if not operation:
            #
            #     raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ошибка повторите еще раз")
            # else:
            #     return {"state": True, "user": ""}
            #
            # # return jsonable_encoder(operation)
            # return jsonable_encoder(operation)
        except:
            print(traceback.format_exc())
            raise HTTPException(status.HTTP_409_CONFLICT, detail="Error no name NameTechTask_key")
            # raise JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'message': "Уже существует запись"})

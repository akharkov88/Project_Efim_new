from datetime import (
    datetime,
    timedelta,
)
import ast
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
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_, not_

import models
import tables
from services.auth import  get_session
from fastapi.encoders import jsonable_encoder

class UserProfileServices:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session


    def create_UserTask(self,UserDATA: models.ModelUserTask ,user: tables.User,) -> tables.ListUserTask:
        try:

            operation = tables.ListUserTask(
                name=UserDATA.name,
                user_create=UserDATA.user_create,
                user_executor=UserDATA.user_executor,
                progress=UserDATA.progress,
                status=UserDATA.status,
                target_date=UserDATA.target_date,
                notification_holder=False,
                notification_executor=True,
                priority=UserDATA.priority,
                user_name=user.username,

            )
            self.session.add(operation)
            self.session.commit()
            operation = (
                self.session
                .query(tables.ListUserTask)
                # .filter(
                #     tables.ListUserTask.customer_id == TechTaskDATA.customer_id,
                # )
                .all()
            )
            if not operation:
                return HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ошибка повторите еще раз")
            # return jsonable_encoder(operation)
            return jsonable_encoder(operation)

        except:
            print(traceback.format_exc())
            raise HTTPException(status.HTTP_409_CONFLICT, detail="Duplicate key")
            # raise JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'message': "Уже существует запись"})

    def get_UserTask(self, user: str) -> tables.ListUserTask:
        try:

            operation = (
                self.session
                .query(tables.ListUserTask)
                .filter(
                    or_(
                    tables.ListUserTask.user_create == user,
                    tables.ListUserTask.user_executor.ilike("%'"+user+"'%"),
                    tables.ListUserTask.user_executor.ilike('%"'+user+'"%')
                )
                )
                .all()
            )

            val_mas=[]
            for hh in jsonable_encoder(operation):
                print(hh["user_create"])
                print(self.get_UserProfile(hh["user_create"]))

                save_val = {}

                if save_val.get(hh["user_create"],False):
                    hh["UserPfofile_create"] = hh["user_create"]
                else:
                    save_val[hh["user_create"]]=self.get_UserProfile(hh["user_create"])
                    hh["UserPfofile_create"] = save_val[hh["user_create"]]

                save_executor = []

                for user_executor_val in ast.literal_eval(hh["user_executor"]):


                    if save_val.get(user_executor_val, False):
                        save_executor.append(save_val[user_executor_val])
                    else:
                        save_val[user_executor_val] = self.get_UserProfile(user_executor_val)
                        save_executor.append(save_val[user_executor_val])

                hh["UserPfofile_executor"] = save_executor

                val_mas.append(hh)


            # if not operation:
            #     return HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ошибка повторите еще раз")
            # return jsonable_encoder(operation)
            return val_mas

        except:
            print(traceback.format_exc())
            raise HTTPException(status.HTTP_409_CONFLICT, detail="Duplicate key")
            # raise JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'message': "Уже существует запись"})

    def update_UserTask(self, user: str,User_data:models.ModelUserTaskUpdate,id:models.ModelUserTaskID) -> tables.ListUserTask:
        try:
            # User_data={'notification_holder': False, 'notification_executor': False}
            # User_data={'notification_holder': True, 'notification_executor': True}
            self.session.query(tables.ListUserTask).filter(tables.ListUserTask.id == id.id).update(dict(User_data))
            self.session.commit()
            operation = (
                self.session
                .query(tables.ListUserTask)
                .filter(
                    tables.ListUserTask.id == id.id
                )
                .first()
            )
            if not operation:
                return HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ошибка повторите еще раз")
            print(jsonable_encoder(operation))
            return jsonable_encoder(operation)

        except:
            print(traceback.format_exc())
            return HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ошибка повторите еще раз")





    def get_UserProfile(self,user:str) -> tables.UserPfofile:
        try:

            # operation = tables.UserPfofile(
            #     user_name=user.username,
            # )
            # self.session.add(operation)
            # self.session.commit()
            operation = (
                self.session
                .query(tables.UserPfofile)
                .filter(
                    tables.UserPfofile.username == user,
                )
                .first()
            )
            if not operation:
                return HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ошибка повторите еще раз")
            # return jsonable_encoder(operation)
            return jsonable_encoder(operation)

        except:
            print(traceback.format_exc())
            raise HTTPException(status.HTTP_409_CONFLICT, detail="Duplicate key")
            # raise JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'message': "Уже существует запись"})
    def set_UserProfile(self,user:str,User_data:models.ModelUserPfofile,) -> tables.UserPfofile:
        try:

            # operation = tables.UserPfofile(
            #     user_name=user.username,
            # )
            # self.session.add(operation)
            # self.session.commit()

            self.session.query(tables.UserPfofile).filter(tables.UserPfofile.username == user).update(dict(User_data))
            self.session.commit()

            operation = (
                self.session
                .query(tables.UserPfofile)
                .filter(
                    tables.UserPfofile.username == user,
                )
                .first()
            )
            if not operation:
                return HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ошибка повторите еще раз")
            # return jsonable_encoder(operation)
            return jsonable_encoder(operation)

        except:
            print(traceback.format_exc())
            raise HTTPException(status.HTTP_409_CONFLICT, detail="Duplicate key")
            # raise JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'message': "Уже существует запись"})

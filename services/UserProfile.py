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


class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


class UserProfileServices:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create_UserTask(self, UserDATA: models.ModelUserTask, user: tables.User, ) -> tables.ListUserTask:
        try:
            val = dict(UserDATA)
            val["user_create"] = user.username
            if ast.literal_eval(val["connection"]) != None:
                if json.loads(val["connection"]).get("UserTasck", False):
                    find_User_tasck = (
                        self.session
                        .query(tables.ListUserTask)
                        .filter(
                            or_(
                                tables.ListUserTask.id == int(json.loads(val["connection"])["UserTasck"]),
                            )
                        )
                        .all()
                    )
                    if not find_User_tasck:
                        return HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ошибка повторите еще раз")

                    if jsonable_encoder(find_User_tasck)[0]["control"] == None:
                        val["control"] = [user.username]
                    else:
                        val["control"] = [user.username]
                        for user_data in jsonable_encoder(find_User_tasck)[0]["control"]:
                            if user_data not in val["control"]:
                                val["control"].append(user_data)

                    for user_data in ast.literal_eval(UserDATA.user_executor):
                        if user_data not in val["control"]:
                            val["control"].append(user_data)
                else:
                    val["control"] = [user.username]
                    for user_data in ast.literal_eval(UserDATA.user_executor):
                        if user_data not in val["control"]:
                            val["control"].append(user_data)

            else:
                    val["control"] = [user.username]
                    for user_data in ast.literal_eval(UserDATA.user_executor):
                        if user_data not in val["control"]:
                            val["control"].append(user_data)


            operation = tables.ListUserTask(**val)
            self.session.add(operation)
            self.session.flush()
            self.session.commit()
            if not operation:
                return HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ошибка повторите еще раз")
            # return jsonable_encoder(find_User_tasck)
            operation2 = (
                self.session
                .query(tables.UserPfofile.last_name, tables.UserPfofile.first_name)
                .filter(
                    tables.UserPfofile.username == user.username
                )
                .first()
            )
            for user_data in ast.literal_eval(UserDATA.user_executor):

                if operation2:
                    try:
                        data = dotdict({"User": user_data,
                                        "Value": f"На Вас назначения задача <{UserDATA.name[UserDATA.name.index(">") + 2:].replace("</a>", "", 1)}> приоритет <{UserDATA.priority.value}> срок выполнения <{UserDATA.target_date}> от <{operation2[0] + " " + operation2[1]}>"})
                    except:
                        data = dotdict({"User": user_data,
                                        "Value": f"На Вас назначения задача <{UserDATA.name}> приоритет <{UserDATA.priority.value}> срок выполнения <{UserDATA.target_date}> от <{operation2[0] + " " + operation2[1]}>"})

                    ClassTelegram.telega_send_message(self, data)
            return self.services_UserTask_Search_id(models.ModelUserTaskID(id=operation.id))

        except:
            print(traceback.format_exc())
            raise HTTPException(status.HTTP_409_CONFLICT, detail="Duplicate key")
            # raise JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'message': "Уже существует запись"})

    def create_UserTaskRoles(self, UserDATA: models.ModelUserTask, user: tables.User, ) -> tables.ListUserTask:
        try:
            user_mas = []
            data = ast.literal_eval(UserDATA.user_executor)
            for user_data in data:
                operation = (
                    self.session
                    .query(tables.User)
                    .filter(
                        or_(
                            tables.User.roles == user_data,
                            tables.User.roles.ilike("%'" + user_data + "'%"),
                            tables.User.roles.ilike('%"' + user_data + '"%')
                        )
                    )
                    .all()
                )
                if operation:
                    for username in operation:
                        if (username.username != user.username):
                            user_mas.append(username.username)
            if user_mas.__len__() == 0:
                raise HTTPException(status.HTTP_409_CONFLICT, detail="Нет пользователей на кого можно назначить")

            val = dict(UserDATA)
            val["user_executor"] = str(user_mas)
            val["user_create"] = user.username
            operation = tables.ListUserTask(**dict(val))
            self.session.add(operation)
            self.session.flush()
            self.session.commit()
            if not operation:
                return HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ошибка повторите еще раз")
            # return jsonable_encoder(operation)
            operation2 = (
                self.session
                .query(tables.UserPfofile.last_name, tables.UserPfofile.first_name)
                .filter(
                    tables.UserPfofile.username == user.username
                )
                .first()
            )
            for user_data in user_mas:
                if operation2:
                    # data = dotdict({"User": user_data, "Value": UserDATA["name"]})
                    try:
                        data = dotdict({"User": user_data,
                                        "Value": f"На Вас назначения задача <{UserDATA.name[UserDATA.name.index(">") + 2:].replace("</a>", "", 1)}> приоритет <{UserDATA.priority.value}> срок выполнения <{UserDATA.target_date}> от <{operation2[0] + " " + operation2[1]}>"})
                    except:
                        data = dotdict({"User": user_data,
                                        "Value": f"На Вас назначения задача <{UserDATA.name}> приоритет <{UserDATA.priority.value}> срок выполнения <{UserDATA.target_date}> от <{operation2[0] + " " + operation2[1]}>"})

                    ClassTelegram.telega_send_message(self, data)
            return jsonable_encoder(operation)

        except:
            print(traceback.format_exc())
            raise HTTPException(status.HTTP_409_CONFLICT, detail="Duplicate key")
            # raise JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'message': "Уже существует запись"})

    def services_UserTask_Search_id(self, id_tasck: models.ModelUserTaskID) -> tables.ListUserTask:
        try:

            operation = (
                self.session
                .query(tables.ListUserTask)
                .filter(
                    tables.ListUserTask.id == id_tasck.id
                )
                .all()
            )

            val_mas = []
            for hh in list(jsonable_encoder(operation)):
                # print(hh["user_create"])
                # print(self.get_UserProfile(hh["user_create"]))

                save_val = {}

                if save_val.get(hh["user_create"], False):
                    hh["UserPfofile_create"] = hh["user_create"]
                else:
                    save_val[hh["user_create"]] = self.get_UserProfile(hh["user_create"])
                    hh["UserPfofile_create"] = save_val[hh["user_create"]]

                save_executor = []

                # print(hh["user_executor"])

                for user_executor_val in ast.literal_eval(hh["user_executor"]):

                    if save_val.get(user_executor_val, False):
                        save_executor.append(save_val[user_executor_val])
                    else:
                        save_val[user_executor_val] = self.get_UserProfile(user_executor_val)
                        save_executor.append(save_val[user_executor_val])

                hh["UserPfofile_executor"] = save_executor

                save_control = []

                for control in hh["control"]:

                    if save_val.get(control, False):
                        save_control.append(save_val[control])
                    else:
                        save_val[control] = self.get_UserProfile(control)
                        save_control.append(save_val[control])

                hh["UserPfofile_control"] = save_control

                val_mas.append(hh)

            # for val in val_mas:
            #     val["create_at"] = dateutil.parser.isoparse(val["create_at"]).strftime("%Y-%m-%d")
            #     if val["user_create"] == user:
            #         val["notification_executor"] = False
            # if not operation:
            #     return HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ошибка повторите еще раз")
            # return jsonable_encoder(operation)
            return val_mas

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
                        tables.ListUserTask.user_executor.ilike("%'" + user + "'%"),
                        tables.ListUserTask.user_executor.ilike('%"' + user + '"%')
                    )
                )
                .all()
            )

            val_mas = []
            for hh in jsonable_encoder(operation):
                # print(hh["user_create"])
                # print(self.get_UserProfile(hh["user_create"]))

                save_val = {}

                if save_val.get(hh["user_create"], False):
                    hh["UserPfofile_create"] = hh["user_create"]
                else:
                    save_val[hh["user_create"]] = self.get_UserProfile(hh["user_create"])
                    hh["UserPfofile_create"] = save_val[hh["user_create"]]

                save_executor = []

                # print(hh["user_executor"])
                for user_executor_val in ast.literal_eval(hh["user_executor"]):

                    if save_val.get(user_executor_val, False):
                        save_executor.append(save_val[user_executor_val])
                    else:
                        save_val[user_executor_val] = self.get_UserProfile(user_executor_val)
                        save_executor.append(save_val[user_executor_val])

                hh["UserPfofile_executor"] = save_executor
                save_control = []
                print(hh["control"])

                for control in hh["control"]:

                    if save_val.get(control, False):
                        save_control.append(save_val[control])
                    else:
                        save_val[control] = self.get_UserProfile(control)
                        save_control.append(save_val[control])

                hh["UserPfofile_control"] = save_control

                val_mas.append(hh)

            for val in val_mas:
                val["create_at"] = dateutil.parser.isoparse(val["create_at"]).strftime("%Y-%m-%d")
                if val["user_create"] == user:
                    val["notification_executor"] = False
            # if not operation:
            #     return HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ошибка повторите еще раз")
            # return jsonable_encoder(operation)
            return val_mas

        except:
            print(traceback.format_exc())
            raise HTTPException(status.HTTP_409_CONFLICT, detail="Duplicate key")
            # raise JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'message': "Уже существует запись"})

    def get_UserTask_Control(self, user: str) -> tables.ListUserTask:
        try:

            operation = (
                self.session
                .query(tables.ListUserTask)
                .filter(
                    tables.ListUserTask.control.any(user)
                )
                .filter(
                    and_(
                        tables.ListUserTask.user_create != user,
                        tables.ListUserTask.user_executor.notlike("%'" + user + "'%"),
                        tables.ListUserTask.user_executor.notlike('%"' + user + '"%')
                    )
                )
                .all()
            )
            val_mas = []
            for hh in jsonable_encoder(operation):

                save_val = {}

                if save_val.get(hh["user_create"], False):
                    hh["UserPfofile_create"] = hh["user_create"]
                else:
                    save_val[hh["user_create"]] = self.get_UserProfile(hh["user_create"])
                    hh["UserPfofile_create"] = save_val[hh["user_create"]]

                save_executor = []

                # print(hh["user_executor"])
                for user_executor_val in ast.literal_eval(hh["user_executor"]):

                    if save_val.get(user_executor_val, False):
                        save_executor.append(save_val[user_executor_val])
                    else:
                        save_val[user_executor_val] = self.get_UserProfile(user_executor_val)
                        save_executor.append(save_val[user_executor_val])

                hh["UserPfofile_executor"] = save_executor

                save_control = []

                for control in hh["control"]:

                    if save_val.get(control, False):
                        save_control.append(save_val[control])
                    else:
                        save_val[control] = self.get_UserProfile(control)
                        save_control.append(save_val[control])

                hh["UserPfofile_control"] = save_control

                val_mas.append(hh)

            for val in val_mas:
                val["create_at"] = dateutil.parser.isoparse(val["create_at"]).strftime("%Y-%m-%d")
                if val["user_create"] == user:
                    val["notification_executor"] = False
            # if not operation:
            #     return HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ошибка повторите еще раз")
            # return jsonable_encoder(operation)
            return val_mas

        except:
            print(traceback.format_exc())
            raise HTTPException(status.HTTP_409_CONFLICT, detail="Duplicate key")
            # raise JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'message': "Уже существует запись"})

    def update_UserTask(self, user: str, User_data: models.ModelUserTaskUpdate,
                        id: models.ModelUserTaskID) -> tables.ListUserTask:
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
            # print(jsonable_encoder(operation))
            return jsonable_encoder(operation)

        except:
            print(traceback.format_exc())
            return HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ошибка повторите еще раз")
    def set_control_UserTask(self, user: str, user_data: models.ModelUserTaskEventControl) -> tables.ListUserTask:
        try:

            operation = (
                self.session
                .query(tables.ListUserTask)
                .filter(
                        tables.ListUserTask.id == user_data.id,
                )
                .first()
            )
            value=jsonable_encoder(operation)
            if user_data.event == "add":
                if user not in value["control"]:

                    value["control"].append(user)
                    User_value = {"control": value["control"]}
                    self.session.query(tables.ListUserTask).filter(tables.ListUserTask.id == user_data.id).update(dict(User_value))
                    self.session.commit()
            if user_data.event == "del":
                if user in value["control"]:
                    value["control"].pop(value["control"].index(user))
                    User_value = {"control": value["control"]}
                    self.session.query(tables.ListUserTask).filter(tables.ListUserTask.id == user_data.id).update(dict(User_value))
                    self.session.commit()




            operation = (
                self.session
                .query(tables.ListUserTask)
                .filter(
                    tables.ListUserTask.id == user_data.id
                )
                .first()
            )
            if not operation:
                return HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ошибка повторите еще раз")
            # print(jsonable_encoder(operation))

            val_mas = []
            # print(hh["user_create"])
            # print(self.get_UserProfile(hh["user_create"]))
            hh=jsonable_encoder(operation)
            save_val = {}

            if save_val.get(hh["user_create"], False):
                hh["UserPfofile_create"] = hh["user_create"]
            else:
                save_val[hh["user_create"]] = self.get_UserProfile(hh["user_create"])
                hh["UserPfofile_create"] = save_val[hh["user_create"]]

            save_executor = []

            # print(hh["user_executor"])

            for user_executor_val in ast.literal_eval(hh["user_executor"]):

                if save_val.get(user_executor_val, False):
                    save_executor.append(save_val[user_executor_val])
                else:
                    save_val[user_executor_val] = self.get_UserProfile(user_executor_val)
                    save_executor.append(save_val[user_executor_val])

            hh["UserPfofile_executor"] = save_executor

            save_control = []

            for control in hh["control"]:

                if save_val.get(control, False):
                    save_control.append(save_val[control])
                else:
                    save_val[control] = self.get_UserProfile(control)
                    save_control.append(save_val[control])

            hh["UserPfofile_control"] = save_control

            val_mas.append(hh)

            # for val in val_mas:
            #     val["create_at"] = dateutil.parser.isoparse(val["create_at"]).strftime("%Y-%m-%d")
            #     if val["user_create"] == user:
            #         val["notification_executor"] = False
            # if not operation:
            #     return HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ошибка повторите еще раз")
            # return jsonable_encoder(operation)
            return val_mas

        except:
            print(traceback.format_exc())
            return HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ошибка повторите еще раз")

    def get_UserProfile(self, user: str) -> tables.UserPfofile:
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

    def set_UserProfile(self, user: str, User_data: models.ModelUserPfofile, ) -> tables.UserPfofile:
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

    def get_getDepartmentTable(self, user: str) -> tables.UserPfofile:
        try:

            operation = (
                self.session
                .query(tables.departmentTable)
                .first()
            )
            if not operation:
                return []
            return jsonable_encoder(operation)

        except:
            print(traceback.format_exc())
            raise HTTPException(status.HTTP_409_CONFLICT, detail="Duplicate key")

    def set_getDepartmentTable(self, user: str, UserDATA: models.ModelgetDepartment) -> tables.departmentTable:
        try:
            if UserDATA.event == "add":
                operation = tables.departmentTable(
                    department=UserDATA.value,
                    username=user,
                )
                self.session.add(operation)
                self.session.commit()

            if UserDATA.event == "del":
                operation2 = (
                    self.session
                    .query(tables.departmentTable)
                    .filter(
                        tables.departmentTable.department == UserDATA.value,
                    )
                    .delete()
                )
                self.session.commit()

            operation = (
                self.session
                .query(tables.departmentTable)
                .all()
            )
            if not operation:
                return list()
            return list(jsonable_encoder(operation))

        except:
            print(traceback.format_exc())
            raise HTTPException(status.HTTP_409_CONFLICT, detail="Duplicate key")

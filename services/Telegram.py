import datetime
import traceback
import traceback


import telebot
from telebot import types

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

class ClassTelegram:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def telega_send_message_group(self,data):


        # return jsonable_encoder(operation)
        bot = telebot.TeleBot('6699554023:AAFv2VuN2NcqydlFlkK5qCpLmCzLL3Euy_g')
        bot.send_message("-1002089164577", data.Value)
        return HTTPException(status.HTTP_200_OK, detail="Ошибка повторите еще раз")

    def telega_send_message(self,data):


        operation = (
            self.session
            .query(tables.UserPfofile)
            .filter(
                tables.UserPfofile.username == data.User
            )
            .first()
        )

        if not operation:
            return HTTPException(status.HTTP_204_NO_CONTENT, detail="Ошибка нет такого пользователя")

        operation = (
            self.session
            .query(tables.User_telegram)
            .filter(
                tables.User_telegram.name_user_telegram == operation.telegram
            )
            .first()
        )
        if not operation:
            return HTTPException(status.HTTP_204_NO_CONTENT, detail="Ошибка нет такого пользователя")

        # return jsonable_encoder(operation)
        bot = telebot.TeleBot('6699554023:AAFv2VuN2NcqydlFlkK5qCpLmCzLL3Euy_g')
        bot.send_message(operation.id_telegram, data.Value)
        return HTTPException(status.HTTP_200_OK,)

    def telega_set_message(self,data):


        operation = tables.User_telegram(
            name_user_telegram=data.name_user_telegram,
            id_telegram=data.id_telegram,
        )
        self.session.add(operation)
        self.session.commit()
        operation = (
            self.session
            .query(tables.User_telegram)
            .filter(
                tables.User_telegram.name_user_telegram == data.name_user_telegram
            )
            .first()
        )
        if not operation:
            raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ошибка повторите еще раз")
        # return jsonable_encoder(operation)
        return HTTPException(status.HTTP_200_OK, detail="Ошибка повторите еще раз")

        # return jsonable_encoder(operation)

        # bot = telebot.TeleBot('6699554023:AAFv2VuN2NcqydlFlkK5qCpLmCzLL3Euy_g')
        # bot.send_message(id, data.Value)

from typing import List

from fastapi import (
    APIRouter,
    Depends,
    status,
    Request,
    Response,
    File,
    UploadFile,
)
from typing import Annotated
from fastapi.responses import FileResponse
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates
from pathlib import Path
import models
import telebot
from telebot import types
import shutil
import os,pathlib

from services.main import (
    TaskServices,
)

from services.Telegram import (
    ClassTelegram,
)
from services.techTaskForm import (
    techTaskFormServices,
)
from services.auth import (
    AuthService,
    get_current_user,
)

router = APIRouter(
    prefix='/message',
    tags=['message'],
)


templates = Jinja2Templates(directory="src/main")


@router.post(
    '/Telegram_send_message',
    # response_model=models.UserTask,
    status_code=status.HTTP_200_OK,
)
def create_operation(
        data: models.BaseTelegram,
        Class_Telegram: ClassTelegram = Depends(),
):
    # Class_Telegram.telega_send_message.delay(data)
    Class_Telegram.telega_send_message(data)
    return Response(status_code=status.HTTP_200_OK)




@router.post(
    '/Telegram_send_message_group',
    # response_model=models.UserTask,
    status_code=status.HTTP_200_OK,
)
def create_operation(
        data: models.BaseTelegram_group,
        Class_Telegram: ClassTelegram = Depends(),
):
    Class_Telegram.telega_send_message_group.delay(data)
    return Response(status_code=status.HTTP_200_OK)




@router.post(
    '/Telegram_set_message',
    # response_model=models.UserTask,
    status_code=status.HTTP_200_OK,
)
def create_operation(
        data: models.BaseUserTelegram,
        Class_Telegram: ClassTelegram = Depends(),
):
    Class_Telegram.telega_set_message.delay(data)
    return Response(status_code=status.HTTP_200_OK)





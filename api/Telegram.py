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

from services.techTaskForm import (
    techTaskFormServices,
)
from services.auth import (
    AuthService,
    get_current_user,
)

router = APIRouter(
    prefix='/techTaskForm',
    tags=['techTaskForm'],
)

templates = Jinja2Templates(directory="src/main")



@router.post(
    '/Telegram_send_message',
    response_model=models.UserTask,
    status_code=status.HTTP_200_OK,
)
def create_operation(
        user_data: models.UserTask,
        Task_Services: techTaskFormServices = Depends(),
):
    return Task_Services.update_value(user_data)



def telega_send_message(id,text):
    bot = telebot.TeleBot('6699554023:AAFv2VuN2NcqydlFlkK5qCpLmCzLL3Euy_g')
    bot.send_message(id, text)

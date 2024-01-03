from typing import List

from fastapi import (
    APIRouter,
    Depends,
    status,
    Request,
    Response,
)
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates

import models

from services.suggest import (
    SuggestServices,
)
from services.main import (
    TaskServices,
)
from services.techTask import (
    TechTaskServices,
)
from services.auth import (
    AuthService,
    get_current_user,
)
from services.main import TaskServices

router = APIRouter(
    prefix='/suggest',
    tags=['suggest'],
)

templates = Jinja2Templates(directory="src/main/")


@router.post(
    '/getSuggest',
    # response_model=models.UserTask,
    status_code=status.HTTP_200_OK,
)
def create_operation(
        user_data: models.CountSuggest,
        Suggest_Services: SuggestServices = Depends(),
        user: models.User = Depends(get_current_user),
):
    return Suggest_Services.get_suggest(user_data,user)

@router.post(
    '/setSuggest',
    # response_model=models.UserTask,
    # status_code=status.HTTP_200_OK,
)
def create_operation(
        user_data: models.SuggestM,
        Suggest_Services: SuggestServices = Depends(),
        user: models.User = Depends(get_current_user),
):
    return Suggest_Services.set_suggest(user_data,user)

@router.post(
    '/deleteSuggest',
    # response_model=models.UserTask,
    # status_code=status.HTTP_200_OK,
)
def create_operation(
        user_data: models.SuggestM,
        Suggest_Services: SuggestServices = Depends(),
        user: models.User = Depends(get_current_user),
):
    return Suggest_Services.delete_suggest(user_data,user)

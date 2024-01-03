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
    prefix='/techTask',
    tags=['techTask'],
)

templates = Jinja2Templates(directory="src/main/")



# @router.get("/formPto")
# async def root(request: Request):
#     return templates.TemplateResponse(
#         "TechTask/techTaskFormEdit_FormNEW.html", {"request": request}
#     )

@router.post(
    '/formPtoCreateUpdate',
    # response_model=models.UserTask,
    # status_code=status.HTTP_200_OK,
)
def create_operation(
        user_data: models.TechTaskPTO,
        Tech_TaskServices: TechTaskServices = Depends(),
        user: models.User = Depends(get_current_user),
):
    return Tech_TaskServices.createTechTaskPTO_S(user_data,user)

@router.post(
    '/formPtoGet',
    # response_model=models.UserTask,
    # status_code=status.HTTP_200_OK,
)
def create_operation(
        user_data: models.BaseTechTaskPTO,
        Tech_TaskServices: TechTaskServices = Depends(),
        user: models.User = Depends(get_current_user),
):
    return Tech_TaskServices.getTechTaskPTO_S(user_data,user)

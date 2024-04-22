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
from fastapi.responses import HTMLResponse, RedirectResponse


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


@router.post(
    '/formPtoGet_key',
    # response_model=models.UserTask,
    # status_code=status.HTTP_200_OK,
)
def create_operation(
        user_data: models.TechTaskPTO_key,
        Tech_TaskServices: TechTaskServices = Depends(),
        user: models.User = Depends(get_current_user),
):
    return Tech_TaskServices.getTechTaskPTO_key_S(user_data,user)


@router.post(
    '/formPtoGet_id',
    # response_model=models.UserTask,
    # status_code=status.HTTP_200_OK,
)
def create_operation(
        user_data: models.TechTaskPTO_id,
        Tech_TaskServices: TechTaskServices = Depends(),
        user: models.User = Depends(get_current_user),
):
    return Tech_TaskServices.getTechTaskPTO_id_S(user_data,user)

# @router.get("/GetWorkingTable_NameTechTask")
# async def GetWorkingTable(request: Request,
#                # NameTechTask: models.WorkingNameTechTask,
#                # Auth_Service: AuthService = Depends(),
#                # Tech_TaskServices: TechTaskServices = Depends(),
#                ):
#     try:
#         # Auth_Service.verify_token(str(request.cookies.get('Authorization')).replace("bearer ", ""))
#         return ""
#     except:
#         return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)
    # return Tech_TaskServices.GetWorkingTable_NameTechTask(NameTechTask)

# @router.get('/GetWorkingTable_NameTechTask',response_model=models.WorkingAll,)
# def get_operationName(request: Request,
#                       NameTechTask: str ,
#                       Auth_Service: AuthService = Depends(),
#                       Tech_TaskServices: TechTaskServices = Depends(),
#                       ):
#     try:
#         user=Auth_Service.verify_token(str(request.cookies.get('Authorization')).replace("bearer ", ""))
#     except:
#         return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)
#     return Tech_TaskServices.GetWorkingTable_NameTechTask(NameTechTask,user)



@router.post('/SetWorkingTable_NameTechTask',
    # response_model=models.Response_WorkingNameTechTask,
    # response_model=models.UserTask,
    # status_code=status.HTTP_200_OK,
)
def SetWorkingTable(
        request: Request,
        user_data: models.WorkingNameTechTask,
        Tech_TaskServices: TechTaskServices = Depends(),
        Auth_Service: AuthService = Depends(),

):
    try:
        user=Auth_Service.verify_token(str(request.cookies.get('Authorization')).replace("bearer ", ""))
    except:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)
    return Tech_TaskServices.SetWorkingTable_NameTechTask(user_data,user)


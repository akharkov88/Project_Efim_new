from typing import List

from fastapi import (
    APIRouter,
    Depends,
    status,
    Request,
    Response,
    Path,
)
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.encoders import jsonable_encoder

from fastapi.responses import FileResponse

from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates

import models,json
import os,pathlib
from services.main import (
    TaskServices,
)
from services.auth import (
    AuthService,
    get_current_user,
)
from services.main import TaskServices
from services.UserProfile import UserProfileServices

router = APIRouter(
    prefix='/main',
    tags=['main'],
)


templates = Jinja2Templates(directory="src/main")



@router.get(
    '/',
    response_model=List[models.Operation],
)
def get_operation(
    request: Request,
    # user: models.User = Depends(get_current_user),
):
    return templates.TemplateResponse(
        "index.html", {"request": request}
    )

@router.get('/old/chart.html',response_model=List[models.Operation],)
def get_operation(request: Request,):
    return templates.TemplateResponse(
        "chart.html", {"request": request}
    )
@router.get('/old/empty.html',response_model=List[models.Operation],)
def get_operation(request: Request,):
    return templates.TemplateResponse(
        "/old/empty.html", {"request": request}
    )
@router.get('/old/form.html',response_model=List[models.Operation],)
def get_operation(request: Request,):
    return templates.TemplateResponse(
        "/old/form.html", {"request": request}
    )
@router.get('/newDesign/newDesign.html',response_model=List[models.Operation],)
def get_operation(request: Request,):
    return templates.TemplateResponse(
        "/newDesign/newDesign.html", {"request": request}
    )
@router.get('/old/tab-panel.html',response_model=List[models.Operation],)
def get_operation(request: Request,):
    return templates.TemplateResponse(
        "/old/tab-panel.html", {"request": request}
    )
@router.get('/old/table.html',response_model=List[models.Operation],)
def get_operation(request: Request,):
    return templates.TemplateResponse(
        "/old/table.html", {"request": request}
    )
@router.get('/old/ui-elements.html',response_model=List[models.Operation],)
def get_operation(request: Request,):
    return templates.TemplateResponse(
        "/old/ui-elements.html", {"request": request}
    )
@router.get('/index.html',response_model=List[models.Operation],)
def get_operation(request: Request,):
    return templates.TemplateResponse(
        "index.html", {"request": request}
    )
@router.get('/old/index_copy_example.html',response_model=List[models.Operation],)
def get_operation(request: Request,):
    return templates.TemplateResponse(
        "/old/index_copy_example.html", {"request": request}
    )

@router.get('/index.html',response_model=List[models.Operation],)
def get_operation(request: Request,):
    return templates.TemplateResponse(
        "index.html", {"request": request}
    )




@router.get('/indexShablon.html',response_model=List[models.Operation],)
def get_operation(request: Request,):
    return templates.TemplateResponse(
        "indexShablon.html", {"request": request}
    )

@router.get('/techTaskForm.html',response_model=List[models.Operation],)
def get_operation(request: Request,):
    return templates.TemplateResponse(
        "TechTask/techTaskForm.html", {"request": request}
    )



@router.get('/Uvedomleniya.html',response_model=List[models.Operation],)
def get_operation(request: Request,):
    return templates.TemplateResponse(
        "Uvedomleniya.html", {"request": request}
    )



@router.get('/ExcelInTable',response_model=List[models.Operation],)
def get_operation(request: Request,):
    return templates.TemplateResponse(
        "ExcelInTable.html", {"request": request}
    )



@router.post(
    '/creatTask',
    response_model=models.UserTask,
    status_code=status.HTTP_200_OK,
)
def create_operation(
        user_data: models.UserTask,
        Task_Services: TaskServices = Depends(),
        user: models.User = Depends(get_current_user),
):
    return Task_Services.createTask_S(user_data,user)

@router.post(
    '/update_value',
    response_model=models.UserTask,
    status_code=status.HTTP_200_OK,
)
def create_operation(
        user_data: models.UserTask,
        Task_Services: TaskServices = Depends(),
):
    return Task_Services.update_value(user_data)


@router.get(
    '/getAllTask',
    response_model=list[models.UserTask],
    status_code=status.HTTP_200_OK,
)
def create_operation(
        Task_Services: TaskServices = Depends(),
):
    return Task_Services.getAllTask_S()

@router.get('/getTechTaskNameTechTask',response_model=models.UserTask,status_code=status.HTTP_200_OK,
)
def create_operation(
        NameTechTask: str,
        Task_Services: TaskServices = Depends(),
):
    return Task_Services.getTechTaskNameTechTask_S(NameTechTask)

@router.get('/getTechTaskIDTechTask',response_model=models.UserTask,status_code=status.HTTP_200_OK,
)
def create_operation(
        ID: str,
        Task_Services: TaskServices = Depends(),
):
    return Task_Services.getTechTaskIDTechTask_S(ID)



# @router.get('/techTaskFormEdit.html',response_model=List[models.Operation],)
# def get_operation(request: Request,NameTechTask: str
#     Task_Services: TaskServices = Depends(),
# ):
#     return templates.TemplateResponse("TechTask/techTaskFormEdit.html", {"request": request,"getAllTask_S":Task_Services.getTechTaskNameTechTask_S(NameTechTask)}
#     )


@router.get('/techTaskFormEdit.html',response_model=List[models.Operation],)
def get_operationName(request: Request,
                      Task_Services: TaskServices = Depends(),
                      NameTechTask: str = "",
                      Auth_Service: AuthService = Depends(),
                      User_ProfileServices: UserProfileServices = Depends(),):
    try:
        user=Auth_Service.verify_token(str(request.cookies.get('Authorization')).replace("bearer ", ""))
    except:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)
    return templates.TemplateResponse(
        "TechTask/techTaskFormEdit.html", {"request": request,"getTechTaskName":Task_Services.getTechTaskNameTechTask_S(NameTechTask),"roles_user":jsonable_encoder(user)["roles"], "get_UserTask": User_ProfileServices.get_UserTask(user.username),"all_user": Auth_Service.get_all_username(),"all_roles":Auth_Service.get_all_roles(),"user":user.username}
    )

@router.get('/techTask.html',response_model=List[models.Operation],)
def get_operation(request: Request,Task_Services: TaskServices = Depends(),):
    return templates.TemplateResponse(
        "TechTask/techTask.html", {"request": request,"getAllTask_S":Task_Services.getAllTask_S()}
    )




@router.get("/adminMenu")
async def root(request: Request):
    return templates.TemplateResponse(
        "adminMenu.html", {"request": request}
    )


@router.get("/techTaskFormEdit_FormNEW")
async def root(request: Request):
    return templates.TemplateResponse(
        "TechTask/techTaskFormEdit_FormNEW.html", {"request": request}
    )


from fastapi import Cookie,Header
@router.get("/qwerty")
async def root( sessionKey: str = Header(None), cookie_param: int | None = Cookie(None)):
    print("sessionKey",sessionKey)
    print("cookie_param",cookie_param)
    return {"message": f"returned"}

from fastapi import Cookie
from typing import Optional
@router.get('/set')
async def setting(response: Response):
    response.set_cookie(key='refresh_token', value='helloworld', httponly=True)
    return True
@router.get('/read')
async def reading(refresh_token: Optional[str] = Cookie(None)):
    print("refresh_token",refresh_token)
    return refresh_token



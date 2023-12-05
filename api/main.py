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
from services.auth import (
    AuthService,
    get_current_user,
)
from services.main import TaskServices

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





@router.get('/main/techTask.html',response_model=List[models.Operation],)
def get_operation(request: Request,Task_Services: TaskServices = Depends(),):
    return templates.TemplateResponse(
        "techTask.html", {"request": request,"getAllTask_S":Task_Services.getAllTask_S()}
    )

@router.get('/techTask.html',response_model=List[models.Operation],)
def get_operation(request: Request,Task_Services: TaskServices = Depends(),):
    return templates.TemplateResponse(
        "TechTask/techTask.html", {"request": request,"getAllTask_S":Task_Services.getAllTask_S()}
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



@router.post(
    '/creatTask',
    response_model=models.BaseTask,
    status_code=status.HTTP_200_OK,
)
def create_operation(
    username: str,
    # user: models.User = Depends(get_current_user),
    Task_Services: TaskServices = Depends(),
):
    # Task_Services.createTask(username)

    # return Response(status_code=Task_Services.createTask(username))
    # val,status=Task_Services.createTask(username)
    # if status==200:
    #     return JSONResponse(content={"message": val.id}, status_code=status)
    # if status!=200:
    return Task_Services.createTask_S(username)

@router.get(
    '/getAllTask',
    response_model=list[models.UserTask],
    status_code=status.HTTP_200_OK,
)
def create_operation(
    # username: str,
    # user: models.User = Depends(get_current_user),
    Task_Services: TaskServices = Depends(),
):
    # Task_Services.createTask(username)

    # return Response(status_code=Task_Services.createTask(username))
    # val,status=Task_Services.createTask(username)
    # if status==200:
    #     return JSONResponse(content={"message": val.id}, status_code=status)
    # if status!=200:
    return Task_Services.getAllTask_S()

# @router.get("/")
# async def root(request: Request):
#     return templates.TemplateResponse(
#         "index.html", {"request": request}
#     )

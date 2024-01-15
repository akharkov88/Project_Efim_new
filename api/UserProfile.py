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

from services.UserProfile import (
    UserProfileServices,
)
from services.auth import (
    AuthService,
    get_current_user,
)
from services.main import TaskServices

router = APIRouter(
    prefix='/userprofile',
    tags=['userprofile'],
)

templates = Jinja2Templates(directory="src/main/")



@router.get('/userprofile',response_model=List[models.Operation],)
def get_operation(request: Request,):
    return templates.TemplateResponse(
        "/UserProfile/UserProfile.html", {"request": request}
    )
@router.get('/UserTask',response_model=List[models.Operation],)
def get_operation(request: Request,):
    return templates.TemplateResponse(
        "/UserProfile/UserTask.html", {"request": request}
    )


@router.post(
    '/createUserTask',
    # response_model=models.UserTask,
    # status_code=status.HTTP_200_OK,
)
def create_operation(
        user_data: models.ModelUserTask,
        Suggest_Services: UserProfileServices = Depends(),
        user: models.User = Depends(get_current_user),
):
    return Suggest_Services.create_UserTask(user_data,user)




@router.get('/Naumov',response_model=List[models.Operation],)
def get_operation(request: Request,):
    return templates.TemplateResponse(
        "/UserProfile/UserTask.html", {"request": request}
    )
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

from services.UserProfile import (
    UserProfileServices,
)
from services.auth import (
    AuthService,
    get_current_user,
)
from services.main import TaskServices
from services.UserProfile import UserProfileServices

router = APIRouter(
    prefix='/userprofile',
    tags=['userprofile'],
)

templates = Jinja2Templates(directory="src/main/")


@router.get('/userprofile', response_model=List[models.Operation], )
def get_operation(request: Request,
                  User_ProfileServices: UserProfileServices = Depends(),
                  # user: models.User = Depends(),
                  Auth_Service: AuthService = Depends(),
                  ):
    try:
        Auth_Service.verify_token(str(request.cookies.get('Authorization')).replace("bearer ", ""))
    except:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)
    return templates.TemplateResponse(
        "/UserProfile/UserProfile.html", {"request": request, "get_UserProfile": User_ProfileServices.get_UserProfile(
            Auth_Service.verify_token(str(request.cookies.get('Authorization')).replace("bearer ", "")).username)}
    )


@router.post('/set_userprofile', response_model=models.ModelUserPfofile)
def set_userprofile(request: Request,
                    User_data: models.ModelUserPfofile,
                    # User_data: models.ModelUserPfofile = Depends(),
                    User_ProfileServices: UserProfileServices = Depends(),
                    # Auth_Service: AuthService = Depends(),
                    user: models.User = Depends(get_current_user),

                    ):
    return User_ProfileServices.set_UserProfile(user.username,User_data)


@router.get('/UserTask', response_model=List[models.Operation], )
def get_operation(request: Request,
                  User_ProfileServices: UserProfileServices = Depends(),
                  Auth_Service: AuthService = Depends(), ):
    try:
        Auth_Service.verify_token(str(request.cookies.get('Authorization')).replace("bearer ", ""))
    except:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)
    return templates.TemplateResponse(
        "/UserProfile/UserTask.html", {"request": request, "get_UserTask": User_ProfileServices.get_UserTask(
            Auth_Service.verify_token(str(request.cookies.get('Authorization')).replace("bearer ", "")).username)}
    )


@router.get('/get_UserTask', response_model=List[models.ModelUserTask], )
def get_operation(request: Request,
                  User_ProfileServices: UserProfileServices = Depends(),
                  Auth_Service: AuthService = Depends(), ):
    try:
        Auth_Service.verify_token(str(request.cookies.get('Authorization')).replace("bearer ", ""))
    except:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)
    return User_ProfileServices.get_UserTask(Auth_Service.verify_token(str(request.cookies.get('Authorization')).replace("bearer ", "")).username)


@router.post(
    '/createUserTask',
    # response_model=models.UserTask,
    # status_code=status.HTTP_200_OK,
)
def create_operation(request: Request,
        user_data: models.ModelUserTask= Depends(),
        UserProfile_Services: UserProfileServices = Depends(),
        user: models.User = Depends(get_current_user),
):
    return UserProfile_Services.create_UserTask(user_data, user)



@router.post('/updateUserTasck', response_model=models.ModelUserTask, )
def update_UserTasck(
        user_data: models.ModelUserTaskUpdate,
        id: models.ModelUserTaskID,
        UserProfile_Services: UserProfileServices = Depends(),
        user: models.User = Depends(get_current_user),
):
    return UserProfile_Services.update_UserTask(user,user_data,id)

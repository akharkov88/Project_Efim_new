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
from filestore import LocalStorage, Store

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

loc = LocalStorage(name='Authorization')


@router.get('/upload_book')
async def upload_book(book=Depends(loc)) -> Store:
    print(111111111111111111111)
    return book.store


@router.get('/upload_book2')
async def root(request: Request):
    return request.cookies.get('Authorization')


@router.get('/upload_book3')
async def root(request: Request, Auth_Service: AuthService = Depends(), ):
    print(Auth_Service.verify_token(request.cookies.get('Authorization').replace("bearer ", "")))
    return request.cookies.get('Authorization')


@router.get('/userprofile', response_model=List[models.Operation], )
def get_operation(request: Request,
                  User_ProfileServices: UserProfileServices = Depends(),
                  # user: models.User = Depends(),
                  Auth_Service: AuthService = Depends(),
                  ):
    return templates.TemplateResponse(
        "/UserProfile/UserProfile.html", {"request": request, "get_UserProfile": User_ProfileServices.get_UserProfile(
            Auth_Service.verify_token(str(request.cookies.get('Authorization')).replace("bearer ", "")).username)}
    )


@router.get('/UserTask', response_model=List[models.Operation], )
def get_operation(request: Request, ):
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
    return Suggest_Services.create_UserTask(user_data, user)


@router.get('/Naumov', response_model=List[models.Operation], )
def get_operation(request: Request, ):
    return templates.TemplateResponse(
        "/UserProfile/UserTask.html", {"request": request}
    )

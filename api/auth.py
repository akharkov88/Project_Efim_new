from fastapi import (
    APIRouter,
    Depends,
    status,
    Request,
)
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates

import models

from services.auth import (
    AuthService,
    get_current_user,
)

router = APIRouter(
    prefix='/auth',
    tags=['auth'],
)

templates = Jinja2Templates(directory="src/auth")


@router.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request}
    )


@router.get("/create")
async def root(request: Request):
    return templates.TemplateResponse(
        "create.html", {"request": request}
    )


@router.get("/Admin_user")
async def root(request: Request):
    return templates.TemplateResponse(
        "Admin_user.html", {"request": request}
    )


@router.post(
    '/sign-up/',
    response_model=models.Token,
    status_code=status.HTTP_201_CREATED,
)
def sign_up(
        user_data: models.UserCreate,
        auth_service: AuthService = Depends(),
):
    return auth_service.register_new_user(user_data)


@router.post(
    '/sign-in/',
    response_model=models.Token,
)
def sign_in(
        auth_data: OAuth2PasswordRequestForm = Depends(),
        auth_service: AuthService = Depends(),
):


    return auth_service.authenticate_user(
        auth_data.username,
        auth_data.password,
    )

# @router.get('/set')
# async def setting(response: Response):
#     response.set_cookie(key='refresh_token', value='helloworld', httponly=True)
#     return True
@router.get(
    '/user/',
    response_model=models.User,
)
def get_user(user: models.User = Depends(get_current_user)):
    return user


@router.get(
    '/get_all_user/',
    response_model=list[models.User],
)
def get_user(user: models.User = Depends(get_current_user),
             auth_service: AuthService = Depends(), ):
    return auth_service.get_all_user(user)



@router.post(
    '/update_roles_user',
)
def get_user(id: int,roles: str,user: models.User = Depends(get_current_user),
             auth_service: AuthService = Depends(),):
    return auth_service.update_user_roles(id,roles)



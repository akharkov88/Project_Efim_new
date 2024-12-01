from typing import List

from fastapi import (
    APIRouter,
    Depends,
    status,
    Request,
    Response,
)
from pydantic import BaseModel, Field, Json
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
import models
import asyncio
from models import ModelUserTaskID
from models.UserProfile import ModelUserTaskEventControl

from services.UserProfile import (
    UserProfileServices,
)
from services.auth import (
    AuthService,
    get_current_user,
)
from services.main import TaskServices
from services.UserProfile import UserProfileServices
from services.searchCompanyINN import SearchCompanyINNServicesClass

router = APIRouter(
    prefix='/searchCompany',
    tags=['searchCompany'],
)

templates = Jinja2Templates(directory="src/main/")


@router.get('/searchCompany', response_model=Json, )
def get_operation(request: Request,
                  param_search: models.ModelSearchCompanyINN = Depends(),
                  SearchCompanyINN: SearchCompanyINNServicesClass = Depends(),
                  Auth_Service: AuthService = Depends(),
                  ):
    try:
        Auth_Service.verify_token(str(request.cookies.get('Authorization')).replace("bearer ", ""))
    except:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)
    return SearchCompanyINN.services_searchCompanyINN(param_search)
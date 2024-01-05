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
@router.get('/Naumov',response_model=List[models.Operation],)
def get_operation(request: Request,):
    return templates.TemplateResponse(
        "/UserProfile/UserTask.html", {"request": request}
    )
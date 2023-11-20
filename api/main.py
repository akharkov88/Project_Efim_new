from typing import List

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
@router.get('/chart.html',response_model=List[models.Operation],)
def get_operation(request: Request,):
    return templates.TemplateResponse(
        "chart.html", {"request": request}
    )
@router.get('/empty.html',response_model=List[models.Operation],)
def get_operation(request: Request,):
    return templates.TemplateResponse(
        "empty.html", {"request": request}
    )
@router.get('/form.html',response_model=List[models.Operation],)
def get_operation(request: Request,):
    return templates.TemplateResponse(
        "form.html", {"request": request}
    )
@router.get('/tab-panel.html',response_model=List[models.Operation],)
def get_operation(request: Request,):
    return templates.TemplateResponse(
        "tab-panel.html", {"request": request}
    )
@router.get('/table.html',response_model=List[models.Operation],)
def get_operation(request: Request,):
    return templates.TemplateResponse(
        "table.html", {"request": request}
    )
@router.get('/ui-elements.html',response_model=List[models.Operation],)
def get_operation(request: Request,):
    return templates.TemplateResponse(
        "ui-elements.html", {"request": request}
    )
@router.get('/index.html',response_model=List[models.Operation],)
def get_operation(request: Request,):
    return templates.TemplateResponse(
        "index.html", {"request": request}
    )

# @router.get("/")
# async def root(request: Request):
#     return templates.TemplateResponse(
#         "index.html", {"request": request}
#     )

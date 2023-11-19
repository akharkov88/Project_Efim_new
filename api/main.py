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
    user: models.User = Depends(get_current_user),
):
    return templates.TemplateResponse(
        "index.html", {"request": request}
    )

# @router.get("/")
# async def root(request: Request):
#     return templates.TemplateResponse(
#         "index.html", {"request": request}
#     )

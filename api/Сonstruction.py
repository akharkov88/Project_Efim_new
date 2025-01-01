from typing import List

from fastapi import (
    APIRouter,
    Depends,
    status,
    Request,
    Response,
)
from pydantic import BaseModel, Field, Json
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
import models

from services.auth import (
    AuthService,
    get_current_user,
)
from services.Сonstruction import СonstructionServicesClass

router = APIRouter(
    prefix='/construction',
    tags=['construction'],
)

templates = Jinja2Templates(directory="src/main/")

#
# @router.get('/searchCompany', response_model=Json, )
# def find_company (request: Request,
#                   param_search: models.ModelCompany = Depends(),
#                   Company: CompanyServicesClass = Depends(),
#                   Auth_Service: AuthService = Depends(),
#                   ):
#     try:
#         Auth_Service.verify_token(str(request.cookies.get('Authorization')).replace("bearer ", ""))
#     except:
#         return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)
#     return Company.services_SearchCompanyINN(param_search)
#
#

@router.get('/addConstruction', ) #, response_model=Json
def save_company(request: Request,
                  param_save: models.ModelConstruction = Depends(),
                  Construction: СonstructionServicesClass = Depends(),
                  Auth_Service: AuthService = Depends(),
                  ):
    try:
        Auth_Service.verify_token(str(request.cookies.get('Authorization')).replace("bearer ", ""))
    except:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)
    return Construction.services_addConstruction(param_save)


@router.get('/updateConstruction', ) #, response_model=Json
def save_company(request: Request,
                  id_construction: models.ModelConstructionID = Depends(),
                  param_save: models.ModelConstruction = Depends(),
                  Construction: СonstructionServicesClass = Depends(),
                  Auth_Service: AuthService = Depends(),
                  ):
    try:
        Auth_Service.verify_token(str(request.cookies.get('Authorization')).replace("bearer ", ""))
    except:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)
    return Construction.updateConstruction(id_construction,param_save)


@router.get('/getConstruction', ) #, response_model=Json
def save_company(request: Request,
                  id_construction:  int = None,
                  page:  int = None,
                  size:  int = None,
                  Construction: СonstructionServicesClass = Depends(),
                  Auth_Service: AuthService = Depends(),
                  ):
    try:
        Auth_Service.verify_token(str(request.cookies.get('Authorization')).replace("bearer ", ""))
    except:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)
    return Construction.services_getConstruction(id_construction,page, size)
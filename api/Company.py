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
from services.Company import CompanyServicesClass

router = APIRouter(
    prefix='/company',
    tags=['company'],
)

templates = Jinja2Templates(directory="src/main/")


@router.get('/searchCompany', response_model=models.CompanyStructureLegal, )
def find_company (request: Request,
                  param_search: models.ModelCompany = Depends(),
                  # modelCompany: models.CompanyStructureLegal = Depends(),
                  filter: str = None,
                  Company: CompanyServicesClass = Depends(),
                  Auth_Service: AuthService = Depends(),
                  ):
    try:
        Auth_Service.verify_token(str(request.cookies.get('Authorization')).replace("bearer ", ""))
    except:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)
    return Company.services_SearchCompanyINN(param_search,filter)


@router.post('/addCompany', response_model=Json, )
def save_company(request: Request,
                  param_save: models.CompanyStructureLegal = Depends(),
                  Company: CompanyServicesClass = Depends(),
                  Auth_Service: AuthService = Depends(),
                  ):
    try:
        Auth_Service.verify_token(str(request.cookies.get('Authorization')).replace("bearer ", ""))
    except:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)
    return Company.services_addCompanyINN(param_save)



@router.get('/getCompany', ) #, response_model=Json
def save_company(request: Request,
                  id_company:  int = None,
                  page:  int = None,
                  size:  int = None,
                  Company: CompanyServicesClass = Depends(),
                  Auth_Service: AuthService = Depends(),
                  ):
    try:
        Auth_Service.verify_token(str(request.cookies.get('Authorization')).replace("bearer ", ""))
    except:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)
    return Company.services_getCompany(id_company,page, size)
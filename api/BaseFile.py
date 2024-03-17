from typing import List

from fastapi import (
    APIRouter,
    Depends,
    status,
    Request,
    Response,
    UploadFile,
)
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates
import os,pathlib
from fastapi.responses import FileResponse

import models
from fastapi.responses import StreamingResponse
from services.main import (
    TaskServices,
)
from services.BaseFile_s import (
    BaseFileServices,
)
from services.auth import (
    AuthService,
    get_current_user,
)
from services.main import TaskServices

router = APIRouter(
    prefix='/BaseFile',
    tags=['BaseFile'],
)

templates = Jinja2Templates(directory="src/main")


@router.get("/download-file/{file_name}")
def download_file(file_name: str,):
    file_location = pathlib.PurePath(pathlib.Path(os.path.abspath(os.getcwd())), "src", "file", file_name)
    # file_location = f'{folder_path}{os.sep}{file_name}'#os.sep is used to seperate with a \
    # return FileResponse(file_location, media_type='application/octet-stream', filename=file_name)
    return FileResponse(path=file_location, filename=file_name, media_type='multipart/form-data')





@router.post("/uploadfile",)
def upload_file(file: UploadFile,user: models.User = Depends(get_current_user),
                BaseFileServices: BaseFileServices = Depends(),):
    # try:
    # for file in file:
    #         # file_path = f"C:\\Users\\gfg/{file.filename}"
    #         # with open(file_path, "wb") as f:
    #         #     f.write(file.file.read())
    #     return {"message": "File saved successfully"}
    # except Exception as e:
    #     return {"message": e.args}
    return BaseFileServices.unload_file(file,user)
@router.post("/getNameFile")
def getNameFile(id: str,BaseFileServices: BaseFileServices = Depends(),):
    # try:
    # for file in file:
    #         # file_path = f"C:\\Users\\gfg/{file.filename}"
    #         # with open(file_path, "wb") as f:
    #         #     f.write(file.file.read())
    #     return {"message": "File saved successfully"}
    # except Exception as e:
    #     return {"message": e.args}
    return BaseFileServices.get_name_file(id)



@router.post(
    '/reports',
)
def getReportss(
        tables: models.Table_excel,
        # user: models.User = Depends(get_current_user),
        BaseFileServices_s: BaseFileServices = Depends(),
):


    file_name=BaseFileServices_s.reports_PTO(tables)

    return file_name


#
# @router.post("/reports",status_code = status.HTTP_200_OK)
# async def getReports(table: models.table_excel,BaseFileServices: BaseFileServices = Depends(),):#url: str,
#     # try:
#     # for file in file:
#     #         # file_path = f"C:\\Users\\gfg/{file.filename}"
#     #         # with open(file_path, "wb") as f:
#     #         #     f.write(file.file.read())
#     #     return {"message": "File saved successfully"}
#     # except Exception as e:
#     #     return {"message": e.args}
#     # return BaseFileServices.reports_PTO()
#
#     # file_location = pathlib.PurePath(pathlib.Path(os.path.abspath(os.getcwd())), "src", "file", file_name)
#
#
#     # return FileResponse(path=BaseFileServices.reports_PTO(), filename="111.xls", media_type='multipart/form-data')
#     # file_name=BaseFileServices.reports_PTO()
#     # file_location = pathlib.PurePath(pathlib.Path(os.path.abspath(os.getcwd())), "src", "file", file_name)
#     # file_location = f'{folder_path}{os.sep}{file_name}'#os.sep is used to seperate with a \
#     # return FileResponse(file_location, media_type='application/octet-stream', filename=file_name)
#     # return FileResponse(path=file_location, filename="file_name.xlsx", media_type='application/vnd.ms-excel')
#     # return Response(BaseFileServices.reports_PTO())
#
#     # file_like = open(file_location, mode="rb")
#     file_name=await BaseFileServices.reports_PTO(table)
#     # file_location = pathlib.PurePath(pathlib.Path(os.path.abspath(os.getcwd())), "src", "file", file_name)
#     # file_location = f'{folder_path}{os.sep}{file_name}'#os.sep is used to seperate with a \
#     # return FileResponse(file_location, media_type='application/octet-stream', filename=file_name)
#     return file_name
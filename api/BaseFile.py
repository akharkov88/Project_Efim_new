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

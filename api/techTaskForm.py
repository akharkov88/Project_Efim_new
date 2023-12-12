from typing import List

from fastapi import (
    APIRouter,
    Depends,
    status,
    Request,
    Response,
    File,
    UploadFile,
)
from typing import Annotated
from fastapi.responses import FileResponse
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates
from pathlib import Path
import models
import shutil
import os,pathlib

from services.main import (
    TaskServices,
)

from services.techTaskForm import (
    techTaskFormServices,
)
from services.auth import (
    AuthService,
    get_current_user,
)

router = APIRouter(
    prefix='/techTaskForm',
    tags=['techTaskForm'],
)

templates = Jinja2Templates(directory="src/main")





# async def chunked_copy(src, dst):
#     await src.seek(0)
#     with open(dst, "wb") as buffer:
#         while True:
#             contents = await src.read(CHUNK_SIZE)
#             if not contents:
#                 # log.info(f"Src completely consumed\n")
#                 break
#             # log.info(f"Consumed {len(contents)} bytes from Src file\n")
#             buffer.write(contents)
#
#
# @router.post("/uploadfile/")
# async def create_upload_file(file: UploadFile = File(...)):
#     fullpath = os.path.join(DESTINATION, file.filename)
#     await chunked_copy(file, fullpath)
#     return {"File saved to disk at": fullpath}

@router.post("/uploadfile")
def upload_file(file: UploadFile,Task_Services: techTaskFormServices = Depends(),):
    # try:
    # for file in file:
    #         # file_path = f"C:\\Users\\gfg/{file.filename}"
    #         # with open(file_path, "wb") as f:
    #         #     f.write(file.file.read())
    #     return {"message": "File saved successfully"}
    # except Exception as e:
    #     return {"message": e.args}
    return Task_Services.unload_file(file)

# @router.post("/uploadfile")
# async def uploadfile(files: list[UploadFile],):
#     # try:
#     #     for file in files:
#     #         file_path = f"C:\\Users\\gfg/{file.filename}"
#     #         with open(file_path, "wb") as f:
#     #             f.write(file.file.read())
#     #             return {"message": "File saved successfully"}
#     # except Exception as e:
#     #     return {"message": e.args}
#     return files

@router.post(
    '/update_value',
    response_model=models.UserTask,
    status_code=status.HTTP_200_OK,
)
def create_operation(
        user_data: models.UserTask,
        Task_Services: techTaskFormServices = Depends(),
):
    return Task_Services.update_value(user_data)


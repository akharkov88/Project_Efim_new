import traceback
from typing import (
    List,
    Optional,
)

from fastapi import (
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

import models
import tables
import os
import pathlib
from services.auth import  get_session
from fastapi.encoders import jsonable_encoder
# from database import get_current_user
#
# print(get_current_user)
class techTaskFormServices:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session
    def unload_file(self,file):
        with open(pathlib.PurePath(pathlib.Path(os.path.abspath(os.getcwd())),"src","file",file.filename), "wb") as f:
            f.write(file.file.read())

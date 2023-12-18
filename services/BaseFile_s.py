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
class BaseFileServices:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session
    def unload_file(self,file,
                    user: tables.User,
                    ) -> str:
        filename=self.create_uuid_table(file.filename,user)
        with open(pathlib.PurePath(pathlib.Path(os.path.abspath(os.getcwd())),"src","file",filename), "wb") as f:
            f.write(file.file.read())
        return filename

    def create_uuid_table(self, name_fail,user: tables.User,) -> tables.BaseFile:
            try:
                operation = tables.BaseFile(
                    name=name_fail,
                    user_name=user.username,

                )
                self.session.add(operation)
                self.session.commit()
                return str(operation.id)
            except:
                print(traceback.format_exc())
                raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Ошибка создания файла")
                # raise JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'message': "Уже существует запись"})

            # return "operation"

    def get_name_file(self,id):
        try:
            operation = (
                self.session
                .query(tables.BaseFile)
                .filter(
                    tables.BaseFile.id == id
                )
                .first()
            )
            #посмотреть какой запрос получится
            print(operation.compile(compile_kwargs={"literal_binds":True}))

            if not operation:
                raise HTTPException(status.HTTP_404)
            # return jsonable_encoder(operation)
            return operation.name
        except:
            print(traceback.format_exc())
            raise HTTPException(status.HTTP_400_BAD_REQUEST)
            # raise JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'message': "Уже существует запись"})

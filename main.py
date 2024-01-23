import uvicorn
from settings import Settings
from api import router
from pathlib import Path
from fastapi.staticfiles import StaticFiles
import os
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.exceptions import HTTPException


async def not_found_error(request: Request, exc: HTTPException):
    return templates.TemplateResponse('404.html', {'request': request}, status_code=404)


async def internal_error(request: Request, exc: HTTPException):
    return templates.TemplateResponse('500.html', {'request': request}, status_code=500)


templates = Jinja2Templates(directory="src/error")

exception_handlers = {
    404: not_found_error,
    500: internal_error
}

app = FastAPI(exception_handlers=exception_handlers)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
app.mount(
    "/static",
    StaticFiles(directory=os.path.join(Path(__file__).parent.parent.absolute() , "Project_Efim_new","src","static")),
    name="static",
)

# from fastapi.responses import HTMLResponse
#
# @app.get("/")
# async def root():
#     return {"greeting":"Hello Harkov"}
#
# @app.get("/items/{item_id}")
# async def read_item(item_id):
#     return {"item_id": item_id}
#
# @app.get("/users/{user_id}")
# async def read_user(user_id: str):
#     return {"Efimov": user_id}
#
# @app.get("/js", response_class=HTMLResponse)
# async def read_items():
#
#     return HTMLResponse(content=open("src/auth.html").read(), status_code=200)

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        reload=True,
        host=Settings.server_host,
        port=Settings.server_port
                )
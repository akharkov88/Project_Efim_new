import uvicorn
from settings import Settings
from fastapi import FastAPI
from api import router
from pathlib import Path
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()
app.include_router(router)
app.mount(
    "/static",
    StaticFiles(directory=os.path.join(Path(__file__).parent.parent.absolute() , "Project_Efim_new2","src","static")),
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
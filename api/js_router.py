# from fastapi import APIRouter, Request
# from fastapi.responses import HTMLResponse
# from pathlib import Path
# from fastapi.staticfiles import StaticFiles
# from fastapi import FastAPI, Request
# from fastapi.templating import Jinja2Templates
#
# import os
#
# router = APIRouter(
#     prefix="/auth",
# )
#
#
# templates = Jinja2Templates(directory="src/auth")
#
#
# @router.get("/")
# async def root(request: Request):
#     return templates.TemplateResponse(
#         "index.html", {"request": request}
#     )
# @router.get("/")
# async def read_user():
#     # return {"Efimov": user_id}
#     # print(open("../src/auth.html").read())
#     return HTMLResponse(content=open("src/auth/index.html",encoding="utf-8").read(), status_code=200)

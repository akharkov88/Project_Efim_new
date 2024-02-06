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


# import telebot
# from telebot import types
import threading

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

# def telega():
#     bot = telebot.TeleBot('6699554023:AAFv2VuN2NcqydlFlkK5qCpLmCzLL3Euy_g')
#
#     # wikipedia.set_lang("ru")
#
#
#     alphabet = ' 1234567890-йцукенгшщзхъфывапролджэячсмитьбюёqwertyuiopasdfghjklzxcvbnm?%.,()!:;'
#
#
#     @bot.message_handler(commands=['start'])
#     def start_message(message):
#         print(message)
#         print(message)
#         bot.send_message(message.chat.id, "Здравствуйте, Сэр.")
#
#     question = ""
#
#     @bot.message_handler(content_types=['text'])
#     def get_text_messages(message):
#         command = message.text.lower()
#         if command == "не так":
#             bot.send_message(message.from_user.id, "а как?")
#             bot.register_next_step_handler(message, wrong)
#         else:
#             global question
#             question = command
#             # reply = "123"
#             # if reply == "вики ":
#             markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
#             item1=types.KeyboardButton("Факт")
#             item2=types.KeyboardButton("Поговорка")
#             markup.add(item1)
#             markup.add(item2)
#             # bot.send_message(message.from_user.id, getwiki(command),  reply_markup=markup)
#             bot.send_message(message.from_user.id, "getwiki(command)",  reply_markup=markup)
#             # else:
#             #     bot.send_message(message.from_user.id, reply)
#
#
#     def wrong(message):
#         a = f"{question},{message.text.lower()} \n"
#         with open('dialogues.txt', "a", encoding='utf-8') as f:
#             f.write(a)
#         bot.send_message(message.from_user.id, "Готово")
#
#
#
#     bot.polling(none_stop=True)
#
# def telega_send_message(id,text):
#     bot = telebot.TeleBot('6699554023:AAFv2VuN2NcqydlFlkK5qCpLmCzLL3Euy_g')
#     bot.send_message(id, text)



if __name__ == '__main__':
    # t1 = threading.Thread(target=telega, args=(), daemon=True)
    # t1.start()
    # telega_send_message("622070505", "getwiki(command)")
    uvicorn.run(
        "main:app",
        reload=True,
        host=Settings.server_host,
        port=Settings.server_port
                )

# 1.-Load module
import asyncio
from database import engine

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from sqlalchemy import URL, create_engine, text, insert, String
from settings import Settings
# from alchemy import sync_session_factory,sync_engine,async_session_factory
import tables
from tables_New_Create import Base

import requests
import json

sync_engine = create_engine(url=Settings.database_url,
                            # echo=True,
                            pool_size=5,  # основные соеденения
                            max_overflow=10,  # дополнтиленые соеденения
                            )  # ensure this is the correct path for the sqlite file.

async_engine = create_async_engine(url=Settings.database_url,
                                   # echo=True,
                                   pool_size=5,  # основные соеденения
                                   max_overflow=10,  # дополнтиленые соеденения
                                   )  # ensure this is the correct path for the sqlite file.

# async def get_123():
#     async with async_engine.connect() as conn:
#         res = await conn.execute(text("SELECT VERSION()"))
#         print(f"{res.first()=}")
# asyncio.run(get_123())

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

def add_user():
    vv = [{"user": {
        "username": "admin",
        "roles": "[\"ADMIN\"]",
        "password": "admin"
    }, "userProfile": {
        "first_name": "AdminАлексей",
        "last_name": "AdminХарьков",
        "telegram": "AlekseyKharkov88",
        "mobile": "890111111-12",
        "worker_tel": "4115566",
        "email": "admin@mail.ru",
        "adress": "улица",
        "office": "пока нет",
        "department": "пока нет"
    }
    }

        , {"user": {
            "username": "Naumov",
            "roles": "[\"ADMIN\"]",
            "password": "Naumov"
        }, "userProfile": {
            "first_name": "Владимир",
            "last_name": "Наумов",
            "telegram": "Frype",
            "mobile": "123",
            "worker_tel": "456",
            "email": "string",
            "adress": "string",
            "office": "string",
            "department": "пока нет"
        }
        },
        {"user": {
            "username": "Efimov",
            "roles": "[\"ADMIN\"]",
            "password": "Efimov"
        }, "userProfile": {
            "first_name": "Илья",
            "last_name": "Ефимов",
            "telegram": "string",
            "mobile": "string",
            "worker_tel": "string",
            "email": "string",
            "adress": "string",
            "office": "string",
            "department": "пока нет"
        }
        }
        , {"user": {
            "username": "Kharkov",
            "roles": "[\"ADMIN\"]",
            "password": "Kharkov"
        }, "userProfile": {
            "first_name": "Алексей",
            "last_name": "Харьков",
            "telegram": "AlekseyKharkov88",
            "mobile": "string",
            "worker_tel": "string",
            "email": "string",
            "adress": "string",
            "office": "string",
            "department": "пока нет"
        }
        }, {"user": {
            "username": "NoAdmin",
            "roles": "[\"\"]",
            "password": "NoAdmin"
        }, "userProfile": {
            "first_name": "Иванов",
            "last_name": "Иван",
            "telegram": "string",
            "mobile": "string",
            "worker_tel": "string",
            "email": "string",
            "adress": "string",
            "office": "string",
            "department": "пока нет"
        }
        }, {"user": {
            "username": "ENGINEER",
            "roles": "[\"ENGINEER\"]",
            "password": "ENGINEER"
        }, "userProfile": {
            "first_name": "ИмяИнженера",
            "last_name": "ФамилияИнженера",
            "telegram": "string",
            "mobile": "string",
            "worker_tel": "string",
            "email": "string",
            "adress": "string",
            "office": "string",
            "department": "пока нет"
        }
        }, {"user": {
            "username": "SUPPLIER",
            "roles": "[\"SUPPLIER\"]",
            "password": "SUPPLIER"
        }, "userProfile": {
            "first_name": "ИмяСнабженца",
            "last_name": "ФамилияСнабженца",
            "telegram": "string",
            "mobile": "string",
            "worker_tel": "string",
            "email": "string",
            "adress": "string",
            "office": "string",
            "department": "пока нет"
        }
        }, {"user": {
            "username": "MAIN_ENGINEER",
            "roles": "[\"MAIN_ENGINEER\"]",
            "password": "MAIN_ENGINEER"
        }, "userProfile": {
            "first_name": "ИмяГлавногоИнженера",
            "last_name": "ФамилияГлавногоИнженера",
            "telegram": "string",
            "mobile": "string",
            "worker_tel": "string",
            "email": "string",
            "adress": "string",
            "office": "string",
            "department": "пока нет"
        }
        }, {"user": {
            "username": "BOSS",
            "roles": "[\"BOSS\"]",
            "password": "BOSS"
        }, "userProfile": {
            "first_name": "ИмяДиректора",
            "last_name": "ФамилияДиректора",
            "telegram": "string",
            "mobile": "string",
            "worker_tel": "string",
            "email": "string",
            "adress": "string",
            "office": "string",
            "department": "пока нет"
        }
        }
    ]
    # vv='username=ad&roles=&password=ad'
    for ff in vv:
        res = requests.post('http://127.0.0.1:8000/auth/sign-up/', json=ff["user"])
        print(res.status_code)


        headers = {'Content-Type': 'application/json', 'Accept': 'application/json',
                   "Authorization": "Bearer " + json.loads(res.text)['access_token']}

        res2 = requests.post('http://127.0.0.1:8000/userprofile/set_userprofile', headers=headers,
                             json=ff["userProfile"])
        print(res2.status_code)
    # print(res.text)

    return json.loads(res.text)['access_token']


token_user = add_user()


# def set_user_profile():
#     headers = {'Content-Type': 'application/x-www-form-urlencoded','Accept': 'application/json'}
#     res = requests.post('http://127.0.0.1:8000/auth/sign-in/', headers=headers, data='grant_type=&username=admin&password=admin&scope=&client_id=&client_secret=')
#     print(res.status_code)
#
# set_user_profile()


async def insert_Suggest():
    value = {"costWork": ["Грунтование м/к", "Изготовление м/к ферм с грунтованием",
                          "Устройство свай недостающих, с армированием и бетонированием", "Окраска м/к ", "Монтаж м/к"],
             "costMaterial": ["Труба проф. 80х3", "Труба проф. 100х3", "Труба6756571 проф. 60х30х2",
                              "Труба656571 проф. 60х30х2", "Труба65енк71 проф. 60х30х2", "Труба657541 проф. 60х30х2",
                              "Трубеа6571 проф. 60х30х2", "Труба6571ку проф. 60х30х2", "Труба655471 проф. 60х30х2",
                              "Труба проф. 60х30х2", "Труба6571 проф. 60х30х2", "Труба16 проф. 60х30х2",
                              "Трубарп1 проф. 60х30х2", "Труба541 проф. 60х30х2", "Труба81 проф. 60х30х2",
                              "Труба7 проф. 60х30х2", "Труба6 проф. 60х30х2", "Труба5 проф. 60х30х2",
                              "Труба4 проф. 60х30х2", "Труба3 проф. 60х30х2", "Труба1 проф. 60х30х2",
                              "Труба11 проф. 60х30х2", "Труба проф. 40х2",
                              "Лист 12", "Лист 10", "Грунт-эмаль 3 в 1", "Распорный анкер М12 (для крепления стоек)",
                              "Труба проф. 60х3"],
             "Special": ["Бурилка", "Манипулятор", "Турвышка 2 шт по 2м"],
             "ListRazdel": ["Земляные работы", "Бетонные работы", "Отделочные работы"],
             "costWorkEdIzm": ["кг", "шт", "м2"],
             "costMaterialEdIzm": ["кг", "шт"],
             "SpecialEdIzm": ["м-см"],
             }

    with sync_engine.connect() as conn:
        for customer_id in value:
            for value_table in value[customer_id]:
                print(value_table)
                # try:
                operation = insert(tables.Suggest).values(
                    value_table=value_table,
                    customer_id=customer_id,
                    user_name="admin",
                )
                conn.execute(operation)
                conn.commit()
                # except:
                #     pass


asyncio.run(insert_Suggest())


async def addRoles():
    value = [
        {"ADMIN": "Администратор"},
        {"ENGINEER": "Инженер"},
        {"MAIN_ENGINEER": "Главный Инженер"},
        {"SUPPLIER": "Снабжение"},
        {"BOSS": "Директор"},
    ]

    with sync_engine.connect() as conn:
        for customer_id in value:
            operation = insert(tables.ListUserRoles).values(
                role=list(customer_id.keys())[0],
                name_roles=customer_id[list(customer_id.keys())[0]],
            )
            conn.execute(operation)
            conn.commit()
            # except:
            #     pass


asyncio.run(addRoles())


async def insert_UserTask():
    vv = [{
        "name": "Разработка таблицы",
        "user_create": "admin",
        "user_executor": "['Naumov','Efimov']",
        "status": "Назначена",
        "result": "",
        "target_date": "2024-01-20",
        "notification_holder": False,
        "notification_executor": True,
        "priority": "Не важно"
    }, {
        "name": "Реализация создание задач",
        "user_create": "admin",
        "user_executor": "['Naumov']",
        "status": "Назначена",
        "result": "",
        "target_date": "2024-01-21",
        "notification_holder": False,
        "notification_executor": True,
        "priority": "Нормально"
    }, {
        "name": "Доделать права в таблицах",
        "user_create": "admin",
        "user_executor": "['Efimov']",
        "status": "Назначена",
        "result": "",
        "target_date": "2024-01-22",
        "notification_holder": False,
        "notification_executor": True,
        "priority": "Важно"
    }, {
        "name": "Доделать права в таблицах",
        "user_create": "Efimov",
        "user_executor": "['admin']",
        "status": "Назначена",
        "result": "",
        "target_date": "2024-01-22",
        "notification_holder": False,
        "notification_executor": True,
        "priority": "Важно"
    }]

    with sync_engine.connect() as conn:
        tables.ListUserTask.__table__.drop(engine)
        Base.metadata.create_all(engine)
        for value_table in vv:
            print(value_table)
            # try:value
            operation = insert(tables.ListUserTask).values(
                value_table
                # name=value_table["name"],
                # user_create=value_table["user_create"],
                # user_executor=value_table["user_executor"],
                # result=value_table["result"],
                # target_date=value_table["target_date"],
                # notification_holder=value_table["notification_holder"],
                # priority=value_table["priority"],
                # progress=value_table["progress"],

            )
            conn.execute(operation)
            conn.commit()
            # except:
            #     pass


asyncio.run(insert_UserTask())

# headers = {'Content-Type': 'application/x-www-form-urlencoded','Accept': 'application/json'}
# #
# #
# res = requests.post('http://127.0.0.1:8000/auth/sign-in/',headers=headers, data="grant_type=&username=admin&password=admin&scope=&client_id=&client_secret=")
# # res = requests.get('http://127.0.0.1:8000/auth/')
# print(res.status_code)
# print(res.text)
# print(json.loads(res.text))
#
# token_user=json.loads(res.text)['access_token']

headers = {'Content-Type': 'application/json', 'Accept': 'application/json', "Authorization": "Bearer " + token_user}
vv = {
    "NameTechTask": "Благостроиство парка",
    "TechTaskClient": "ООО ЖилСтройБыт",
    "TechTaskProject": '[{"name":"github (1) (1).txt","id":"cc70a1ce-f190-4259-87c8-8527df5df082","value_user":"test_file"}]',
    "TechTaskPPR": "string",
    "TechTaskOverhead": "string",
    "TechTaskDateKP": "2024-02-07",
    "TechTaskDateEndWork": "2024-02-08",
    "TechTaskPrice": "string",
    "TechTaskLeaderKP": "string"
}

# vv='username=ad&roles=&password=ad'
res = requests.post('http://127.0.0.1:8000/main/creatTask/', headers=headers, json=vv)
print(res.status_code)
# print(res.text)

vv = [
    {"name_user_telegram": "AlekseyKharkov88",
     "id_telegram": "622070505"},
    {"name_user_telegram": "Frype",
     "id_telegram": "379116309"}
]

for v in vv:
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    # vv='username=ad&roles=&password=ad'
    res = requests.post('http://127.0.0.1:8000/message/Telegram_set_message/', headers=headers, json=v)
    print(res.status_code)

user={
        "username": "admin",
        "roles": "[\"ADMIN\"]",
        "password": "admin"
}


headers = {'Content-Type': 'application/x-www-form-urlencoded','Accept': 'application/json'}
#
#
res = requests.post('http://127.0.0.1:8000/auth/sign-in/',headers=headers, data="grant_type=&username=admin&password=admin&scope=&client_id=&client_secret=")
access_token=json.loads(res.text)
def add_department():
    global access_token
    vv=[
        {
          "value": "отдел снабжения",
          "event": "add"
        },
        {
          "value": "отдел закупки",
          "event": "add"
        }
    ]

    for ff in vv:
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json',
                   "Authorization": "Bearer " + access_token["access_token"]}

        res = requests.post('http://127.0.0.1:8000/userprofile/setDepartmentTable', headers=headers, json=ff)
        print(res.status_code)
add_department()
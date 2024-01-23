# 1.-Load module
import asyncio
from  database import engine

from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker,AsyncSession
from sqlalchemy.orm import Session,sessionmaker,DeclarativeBase
from sqlalchemy import URL,create_engine,text,insert,String
from settings import Settings
# from alchemy import sync_session_factory,sync_engine,async_session_factory
import tables
from  tables_New_Create import Base


import requests
import json

sync_engine=create_engine(url=Settings.database_url,
                     # echo=True,
                     pool_size=5,# основные соеденения
                     max_overflow=10,# дополнтиленые соеденения
                     ) # ensure this is the correct path for the sqlite file.

async_engine=create_async_engine(url=Settings.database_url,
                     # echo=True,
                     pool_size=5,# основные соеденения
                     max_overflow=10,# дополнтиленые соеденения
                     ) # ensure this is the correct path for the sqlite file.


# async def get_123():
#     async with async_engine.connect() as conn:
#         res = await conn.execute(text("SELECT VERSION()"))
#         print(f"{res.first()=}")
# asyncio.run(get_123())

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

def add_user():
    headers = {'Content-Type': 'application/json','Accept': 'application/json'}
    vv=[{
      "username": "admin",
      "roles": "[\"Admin\"]",
      "password": "admin"
    },{
      "username": "Naumov",
      "roles": "[\"Admin\"]",
      "password": "Naumov"
    },{
      "username": "Efimov",
      "roles": "[\"Admin\"]",
      "password": "Efimov"
    },{
      "username": "Kharkov",
      "roles": "[\"Admin\"]",
      "password": "Kharkov"
    }]
    # vv='username=ad&roles=&password=ad'
    for ff in vv:
        res = requests.post('http://127.0.0.1:8000/auth/sign-up/',json=ff)
        print(res.status_code)
        # print(res.text)
    return json.loads(res.text)['access_token']



token_user=add_user()
async def insert_Suggest():
    value = {"costWork": ["Грунтование м/к", "Изготовление м/к ферм с грунтованием",
                       "Устройство свай недостающих, с армированием и бетонированием", "Окраска м/к ", "Монтаж м/к"],
          "costMaterial": ["Труба проф. 80х3", "Труба проф. 100х3", "Труба проф. 60х30х2", "Труба проф. 40х2",
                           "Лист 12", "Лист 10", "Грунт-эмаль 3 в 1", "Распорный анкер М12 (для крепления стоек)",
                           "Труба проф. 60х3"],
          "Special": ["Бурилка", "Манипулятор", "Турвышка 2 шт по 2м"],
          "ListRazdel": ["Земляные работы", "Бетонные работы", "Отделочные работы"],
          "costWorkEdIzm": ["кг", "шт", "м2"],
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
},{
  "name": "Реализация создание задач",
  "user_create": "admin",
  "user_executor": "['Naumov']",
  "status": "Назначена",
  "result": "",
  "target_date": "2024-01-21",
  "notification_holder": False,
  "notification_executor": True,
  "priority": "Нормально"
},{
  "name": "Доделать права в таблицах",
  "user_create": "admin",
  "user_executor": "['Efimov']",
  "status": "Назначена",
  "result": "",
  "target_date": "2024-01-22",
  "notification_holder": False,
  "notification_executor": True,
  "priority": "Важно"
},{
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
#
#
# res = requests.post('http://127.0.0.1:8000/auth/sign-in/',headers=headers, data="grant_type=&username=admin&password=admin&scope=&client_id=&client_secret=")
# # res = requests.get('http://127.0.0.1:8000/auth/')
# print(res.status_code)
# print(res.text)
# print(json.loads(res.text))
#
# token_user=json.loads(res.text)['access_token']

headers = {'Content-Type': 'application/json','Accept': 'application/json',"Authorization": "Bearer " + token_user}
vv={
  "NameTechTask": "Благостроиство парка",
  "TechTaskClient": "ООО ЖилСтройБыт",
  "TechTaskProject": "string",
  "TechTaskPPR": "string",
  "TechTaskOverhead": "string",
  "TechTaskDateKP": "string",
  "TechTaskDateEndWork": "string",
  "TechTaskPrice": "string",
  "TechTaskLeaderKP": "string"
}
# vv='username=ad&roles=&password=ad'
res = requests.post('http://127.0.0.1:8000/main/creatTask/',headers=headers,json=vv)
print(res.status_code)
# print(res.text)


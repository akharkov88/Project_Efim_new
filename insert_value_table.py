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


async def get_123():
    async with async_engine.connect() as conn:
        res = await conn.execute(text("SELECT VERSION()"))
        print(f"{res.first()=}")
asyncio.run(get_123())

async def insert_data2(value):
    with sync_engine.connect() as conn:
        tables.Suggest.__table__.drop(engine)
        Base.metadata.create_all(engine)
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

vv={"costWork":["Грунтование м/к","Изготовление м/к ферм с грунтованием","Устройство свай недостающих, с армированием и бетонированием" ,"Окраска м/к " ,"Монтаж м/к"],
    "costMaterial":["Труба проф. 80х3","Труба проф. 100х3","Труба проф. 60х30х2","Труба проф. 40х2","Лист 12" ,"Лист 10" ,"Грунт-эмаль 3 в 1","Распорный анкер М12 (для крепления стоек)","Труба проф. 60х3"],
    "Special":["Бурилка" ,"Манипулятор","Турвышка 2 шт по 2м"],
    "ListRazdel":["Земляные работы" ,"Бетонные работы","Отделочные работы"],
    "costWorkEdIzm":["кг", "шт", "м2"],
    }
asyncio.run(insert_data2(vv))

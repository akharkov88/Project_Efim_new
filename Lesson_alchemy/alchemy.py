# 1.-Load module
import asyncio

from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker,AsyncSession
from sqlalchemy.orm import Session,sessionmaker,DeclarativeBase
from sqlalchemy import URL,create_engine,text,insert,String
from config import settings
from typing import Annotated
# from model_alchemy import metadata_obj,workers_table
# from model_alchemy import WorkersORM


sync_engine=create_engine(url=settings.database_url_psycopg,
                     # echo=True,
                     pool_size=5,# основные соеденения
                     max_overflow=10,# дополнтиленые соеденения
                     ) # ensure this is the correct path for the sqlite file.

async_engine=create_async_engine(url=settings.database_url_psycopg,
                     # echo=True,
                     pool_size=5,# основные соеденения
                     max_overflow=10,# дополнтиленые соеденения
                     ) # ensure this is the correct path for the sqlite file.
# async def get_123():
#     async with async_engine.connect() as conn:
#         res = await conn.execute(text("SELECT VERSION()"))
#         print(f"{res.first()=}")
# asyncio.run(get_123())

# def create_table():
#     metadata_obj.drop_all(sync_engine)
#     metadata_obj.create_all(sync_engine)
#
# create_table()
sync_session_factory = sessionmaker(sync_engine)
async_session_factory = async_sessionmaker(async_engine)

str256=Annotated[str,256]
class Base(DeclarativeBase):
    type_anotachon_map={
        str256:String(256)
    }
    pass

# async def insert_data():
#     async with async_engine.connect() as conn:
#         stmt="INSERT INTO workers (username) VALUES  ('Boobr'),('Doobr');"
#         await conn.execute(text(stmt))
#         await conn.commit()
#
# asyncio.run(insert_data())
#
# async def insert_data():
#     async with async_engine.connect() as conn:
#         stmt = insert(workers_table).values([{"username":"wwww"},{"username":"wewewe"}])
#         await conn.execute(stmt)
#         await conn.commit()
#
# asyncio.run(insert_data())



# with sync_engine.connect() as conn:
#     res = conn.execute(text("SELECT VERSION()"))
#     print(f"{res.first()=}")

# print(settings.database_url_psycopg)
#3.- Read data with pandas

#4.- I also want to add a new table from a dataframe in sqlite (a small one)

# df_todb.to_sql(name = 'newTable',con= dbEngine, index=False, if_exists='replace')




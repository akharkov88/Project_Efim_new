from model_alchemy import metadata_obj
from alchemy import sync_session_factory,sync_engine,async_session_factory
from model_alchemy import WorkersORM
import asyncio

#
def create_table():
    metadata_obj.drop_all(sync_engine)
    metadata_obj.create_all(sync_engine)

create_table()
async def insert_data2():
    async with async_session_factory() as Session:
        wolk=WorkersORM(username="bobr_orm")
        Session.add(wolk)

        kot=WorkersORM(username="kot_orm")
        pes=WorkersORM(username="pes_orm")
        Session.add_all([kot,pes])
        await Session.commit()

asyncio.run(insert_data2())
from aiogram.utils import executor
from Bot_transport_lib import dp
from Handlers import client, admin, general
from data_base import sqlite_db

async def on_startup(_):
    print('Бот вышел в онлайн')
    sqlite_db.sql_start()



client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
general.register_handlers_general(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

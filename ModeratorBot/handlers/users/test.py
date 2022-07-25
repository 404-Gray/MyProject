from aiogram import types

from keyboards.default import kb_test
from loader import dp

@dp.message_handler()#text='/menu' - если что допосать определённую команду для открытия кнопки меню
async def test(message: types.Message):
    await message.answer('Такой команды нет! Меню тебе в помощь.', reply_markup=kb_test)
#message.from_user.full_name - обрашение по полному имени
#message.from_user.first_name - обращение по имени
#message.from_user.last_name - обращение по фамилии
#message.from_user.id - обращение по личному id
#message.from_user.url - обращение по личной телеграм ссылке
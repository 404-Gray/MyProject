from aiogram import types

from keyboards.inline import ikb_menu
from loader import dp


@dp.message_handler(text='Инлайн меню')
async def show_inline_menu(message: types.Message):
    await message.answer('Ты выбрал инлайн меню \nВыбирай дальше', reply_markup=ikb_menu)

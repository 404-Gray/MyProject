from aiogram import types
from loader import dp

@dp.message_handler(text='/help')
async def command_help(message: types.Message):
    await message.answer(f'Приветствую {message.from_user.full_name}! \n'
                         f'Для входа в инлайн меню напиши "Инлайн меню"\n'
                         f'Для начала регистрации напиши "/register"')
from aiogram import types
from loader import dp
from filters import IsPrivate, IsCommon
from utils.misc import rate_limit


@rate_limit(limit=10, key='/start')
@dp.message_handler(text='/start')
async def command_start(message: types.Message):
    await message.answer(f'Приветствую {message.from_user.full_name}! \n'
                         f'Твой id {message.from_user.id}')
#message.from_user.full_name - обрашение по полному имени
#message.from_user.first_name - обращение по имени
#message.from_user.last_name - обращение по фамилии
#message.from_user.id - обращение по личному id
#message.from_user.url - обращение по личной телеграм ссылке
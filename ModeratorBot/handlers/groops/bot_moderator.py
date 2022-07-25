from aiogram import types
import string
from data import config
from data.config import banned_messages
from filters import IsCommon

from loader import dp
from utils.misc import rate_limit


@rate_limit(0, 'groups')
@dp.message_handler(IsCommon())
async def forbidden_words(message: types.Message):
    if {i.lower().translate(str.maketrans("", "", string.punctuation)) for i in message.text.split(' ')} \
            .intersection(set(banned_messages)) != set():
        await message.reply('Ругаться запрещено!')  # выводим предупреждение
        await message.delete()

@rate_limit(0, 'groups')
@dp.message_handler(IsCommon())
async def check_messages(message: types.Message):
    text = message.text.lower().replace(' ', '')
    for banned_message in config.banned_messages:
        if banned_message in text:
            await message.delete()




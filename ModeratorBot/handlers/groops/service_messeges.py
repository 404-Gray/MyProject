from aiogram import types

from filters import IsCommon
from loader import dp, bot
from utils.misc import rate_limit


@rate_limit(limit=0, key='groups')
@dp.message_handler(IsCommon(), content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def welcome_message(message: types.Message):
    members = ', '.join([mess.get_mention(as_html=True) for mess in message.new_chat_members])
    await message.reply(f'Привет {members} 👋')


@rate_limit(limit=0, key='groups')
@dp.message_handler(IsCommon(), content_types=types.ContentType.LEFT_CHAT_MEMBER)
async def left_chat_member(message: types.Message):

    # Если пользователь покинул чат добровольно
    if message.left_chat_member.id == message.from_user.id:
        await message.reply(f'{message.left_chat_member.get_mention(as_html=True)} покинул(-ла) чат 🤦‍♂️.')
    # Если его кто то выгнал
    else:
        await message.reply(f'{message.left_chat_member.get_mention(as_html=True)} был удалён из чата Высшими Силами.')

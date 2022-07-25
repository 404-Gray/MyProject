from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from loader import bot


class IsAdmin(BoundFilter):
    async def chek(self, message: types.Message):
        chat_member = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
        admin_types = [types.ChatMemberStatus.ADMINISTRATOR, types.ChatMemberStatus.CREATOR]
        return chat_member.status in admin_types

from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsCommon(BoundFilter):
    async def check(self, message: types.Message):
        group_types = [types.ChatType.GROUP, types.ChatType.SUPERGROUP]
        return message.chat.type in group_types

from aiogram import Dispatcher
from .private_chat import IsPrivate
from .groups_chat import IsCommon
from .group_admin import IsAdmin


def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsPrivate)
    dp.filters_factory.bind(IsCommon)
    dp.filters_factory.bind(IsAdmin)
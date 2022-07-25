from aiogram import Dispatcher
from .trottling import ThrottlingMiddleware


def setup(dp: Dispatcher):
    dp.middleware.setup(ThrottlingMiddleware())

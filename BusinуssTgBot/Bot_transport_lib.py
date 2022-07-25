from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

'''MemoryStorage - используем самый простой способ хранения дынных, данные хранятся в оперативной памяти
aiogram так же поддерживает базы данных "MONGO" и "AIOREDIS'''
storage = MemoryStorage()

bot = Bot('5461760280:AAGa0355zuzubioERmAepyNq5OlmIZsDlrY')  # активируем бота токеном
# Диспетчер для бота, в aiogram хэндлерами управляет диспетчер
dp = Dispatcher(bot, storage=storage)

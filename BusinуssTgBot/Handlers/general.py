from aiogram import types, Dispatcher
from Bot_transport_lib import dp
import json
import string


# запретим использовать матерные слова
@dp.message_handler()
async def forbidden_words(message: types.Message):
    # необходимо очистить слова от маскирующих символов
    # получаем сообщение и разбиваем по разделителю - message.text
    # каждое слово обрабатываем приводя к нижнему регистру и убираем маскирующие символы
    if {i.lower().translate(str.maketrans("", "", string.punctuation)) for i in message.text.split(' ')} \
            .intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply('Ругаться запрещено!')  # выводим предупреждение
        await message.delete()  # удаляем матерное сообщение


def register_handlers_general(dp: Dispatcher):
    dp.register_message_handler(forbidden_words)

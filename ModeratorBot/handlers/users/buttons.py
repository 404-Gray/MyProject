from aiogram import types

from handlers.users.inline_menu import show_inline_menu
from loader import dp


@dp.message_handler(text='Список команд')
async def button_one(message: types.Message):
    await message.reply(f'{message.from_user.first_name}, '
                        f'вот список доступных команд для тестирования:\n'
                        f'/start - запускает бота и вносит данные пользователя в БД\n'
                        f'/help - типа помощь, кроме текста функционала не несёт\n'
                        f'/register - регистрация - запускает машину состояний без вноса данных в БД\n'
                        f'"отмена" - отменяет предыдущую команду\n'
                        f'/ref - вывод реферальной ссылки \n'
                        f'/profile - вывод информации о пользователе из БД\n'
                        f'/ban и /unban - команды есть но не настроены под пользователя\n'
                        f'"Инлайн меню" - вывод инлайн кнопочек\n'
                        f'/mailing - рассылка (для администратов)\n')



@dp.message_handler(text='Вторая кнопка')
async def button_two(message: types.Message):
    await message.answer(f'Отлично {message.from_user.full_name}! \n'
                         f'Ты выбрал второй раздел')


@dp.message_handler(text='Третья кнопка')
async def button_three(message: types.Message):
    await message.answer(f'Отлично {message.from_user.full_name}! \n'
                         f'Ты выбрал третий раздел')


@dp.message_handler(text='Четвёртая кнопка')
async def button_four(message: types.Message):
    await message.answer(f'Отлично {message.from_user.full_name}! \n'
                         f'Ты выбрал четвёртый раздел')


@dp.message_handler(text='Пятая кнопка')
async def button_five(message: types.Message):
    await message.answer(f'Отлично {message.from_user.full_name}! \n'
                         f'Ты выбрал пятый раздел')


@dp.message_handler(text='Инлайн меню')
async def button_six():
    await show_inline_menu()

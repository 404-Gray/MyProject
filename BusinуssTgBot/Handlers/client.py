from aiogram import types, Dispatcher
from Bot_transport_lib import bot
from Bot_transport_lib import dp
from data_base import sqlite_db
from keyboards import kb_client

@dp.message_handler(commands=['start', 'старт'])
async def start_commands(message: types.message):
    try:  # если сообщение не отправится в личку удалим сообщение
        await bot.send_message(message.from_user.id, '<Приветствие>, для помощи введите /help или /помощь',
                               reply_markup=kb_client)
        await message.delite()
    except:
        await message.reply('<Приветствие>, \nдля помощи введите /help или /помощь')


@dp.message_handler(commands=['help', 'помощь'])
async def help_commands(message: types.message):
    await message.reply('Общение с ботом в лс, напишите ему \nhttps://t.me/Template_telebot '
                        '\nДругая информация для помощи')


@dp.message_handler(commands=['open_time', 'режим_работы'])
async def open_time_command(message: types.message):
    await bot.send_message(message.from_user.id, '<режим_работы>')


@dp.message_handler(commands=['address', 'адрес'])
async def address_command(message: types.message):
    await bot.send_message(message.from_user.id, '<адрес>')

@dp.message_handler(commands=['меню', 'menu'])
async def menu_command(message: types.Message):
    await sqlite_db.sql_read(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_commands, commands=['start', 'старт'])
    dp.register_message_handler(help_commands, commands=['help', 'помощь'])
    dp.register_message_handler(open_time_command, commands=['open_time', 'режим_работы'])
    dp.register_message_handler(address_command, commands=['address', 'адрес'])
    dp.register_message_handler(menu_command, commands=['menu', 'меню'])

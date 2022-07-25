from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


'''Кнопки управления админа'''
button_load = KeyboardButton('/загрузить')
button_del = KeyboardButton('/удалить')
button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load).add(button_del)

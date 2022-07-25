from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn1 = KeyboardButton('/open_time')
btn2 = KeyboardButton('/address')
btn3 = KeyboardButton('/menu')
btn4 = KeyboardButton('Указать свой номер', request_contact=True)
btn5 = KeyboardButton('Указать своё местоположение', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(btn3).row(btn1, btn2).row(btn4, btn5)

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Список команд'),
            KeyboardButton(text='Вторая кнопка')
        ],
        [
            KeyboardButton(text='Третья кнопка')
        ],
        [
            KeyboardButton(text='Четвёртая кнопка'),
            KeyboardButton(text='Пятая кнопка'),
            KeyboardButton(text='Инлайн меню')
        ]
    ],
    resize_keyboard=True
)

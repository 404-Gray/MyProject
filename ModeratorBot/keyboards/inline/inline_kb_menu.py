from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# row_width - это количество кнопок в одной строке
ikb_menu = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Сообщение', callback_data='Это тестовая кнопка'),
                                        InlineKeyboardButton(text='Ссылка', url='https://itoverone.by/'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='Наш Мастер-Джедай', url='https://www.linkedin.com/in/listopaddenis/')
                                    ]
                                ])

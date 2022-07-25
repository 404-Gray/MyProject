from aiogram.types import ContentType, Message, InputFile
from loader import dp


@dp.message_handler(content_types=ContentType.PHOTO)
async def send_photo_file_id(message: Message):
    await message.answer(message.photo[-1].file_id)


@dp.message_handler(text='/photo')
async def send_photo(message: Message):
    photo_bytes = InputFile(path_or_bytesio='media/photo1.jpg')

    await dp.bot.send_photo(chat_id=message.chat.id, photo=photo_bytes)

from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from loader import dp
from filters import IsPrivate
from utils.db_api import quick_commands as commands
from utils.misc import rate_limit


@rate_limit(limit=3, key='/start')
@dp.message_handler(IsPrivate(), CommandStart())
async def command_start(message: types.Message):
    args = message.get_args()
    print(args)
    new_args = await commands.check_args(args, message.from_user.id)
    print(new_args)
    try:
        user = await commands.select_user(message.from_user.id)
        if user.status == 'active':
            await message.answer(f'Привет {message.from_user.first_name}\n'
                                 f'Ты уже зарегестрирован.')
        elif user.status == 'baned':
            await message.answer('Ты забанен')
    except Exception:
        await commands.add_user(user_id=message.from_user.id,
                                first_name=message.from_user.first_name,
                                last_name=message.from_user.last_name,
                                username=message.from_user.username,
                                referral_id=int(new_args),
                                status='activ')
        await message.answer('Ты успешно зарегистрирован')


@rate_limit(limit=10)
@dp.message_handler(IsPrivate(), text='/ban')
async def get_ban(message: types.Message):
    await commands.update_status(user_id=message.from_user.id, status='baned')
    await message.answer('Ты забанен.')


@rate_limit(limit=10)
@dp.message_handler(IsPrivate(), text='/unban')
async def get_unban(message: types.Message):
    await commands.update_status(user_id=message.from_user.id, status='activ')
    await message.answer('Тебя разбанили')


@rate_limit(limit=10)
@dp.message_handler(IsPrivate(), text='/profile')
async def profile(message: types.Message):
    user = await commands.select_user(message.from_user.id)
    await message.answer(f'id - {user.user_id}\n'
                         f'first_name - {user.first_name}\n'
                         f'last_name - {user.last_name}\n'
                         f'username - {user.username}\n'
                         f'status - {user.status}')

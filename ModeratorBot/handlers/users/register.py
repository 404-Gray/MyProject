from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text

from filters import IsPrivate
from loader import dp

from states import register


@dp.message_handler(IsPrivate(), Command('register'))  # Когда бот получит команду /register будет выполняться хэндлер
async def register_(message: types.Message):
    await message.answer(f'Ты начал регистрацию! \nЧто бы её прервать напиши "отмена" \n'
                         f'Введи свои данные: Фамилию Имя и Отчество')
    await register.part1.set()  # состояние ввода имени


@dp.message_handler(state='*', text='отмена')
@dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Регистрация отменена!')


@dp.message_handler(state=register.part1)  # ловим сюда сообщение о первом состоянии (await register.part1.set())
async def part1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(part1=answer)
    await message.answer(f'{answer}, теперь укажи свой номер телефона')
    await register.part2.set()


@dp.message_handler(state=register.part2)  # ловим сюда сообщение о втором состоянии (await register.part2.set())
async def part2(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(part2=answer)
    await message.answer('И последнее. Укажи свою почту!')
    await register.part3.set()


@dp.message_handler(state=register.part3)  # ловим сюда сообщение о втором состоянии (await register.part3.set())
async def part3(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(part3=answer)
    data = await state.get_data()
    name = data.get('part1')
    phone_number = data.get('part2')
    mail = data.get('part3')
    await message.answer(f'Мини-регистрация завершена.\n'
                         f'Твоё имя - {name},\n'
                         f'Твой номер - {phone_number},\n'
                         f'Твоя почта - {mail}')
    await state.finish()

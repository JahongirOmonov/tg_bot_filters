from aiogram import types
from loader import dp
from aiogram.dispatcher.filters import state, Text
from aiogram.dispatcher import FSMContext



@dp.message_handler(Text(equals="Byden"))
async def bot_state(message: types.Message, state: FSMContext):
    await state.set_state('tanlovda')
    await message.answer(f"Kerakli mahsulotni tanlang! ")

@dp.message_handler(state='tanlovda')
async def bot_state(message: types.Message, state: FSMContext):
    # await state.set_state('mahsulot')
    await message.answer(f"Mahsulot tanlandi")


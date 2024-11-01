from aiogram import types
from loader import dp

@dp.message_handler(hashtags=['savol'])
async def bot_hastag(message: types.Message):
    await message.answer(f"Qanaqa savol?")


@dp.message_handler(cashtags=['usd', 'uzs'])
async def bot_hastag(message: types.Message):
    await message.answer(f"Qanaqa USD?")



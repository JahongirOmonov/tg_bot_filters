from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp

@dp.message_handler(CommandStart(deep_link='kunuz'))
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}! siz kunuz orqali qabul qilindiz!")


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")







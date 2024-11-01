from aiogram import types
from loader import dp
from aiogram.dispatcher.filters import Regexp

EMAIL = r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"


@dp.message_handler(Regexp(EMAIL))
async def bot_regex(message: types.Message):
    await message.answer(f"Emailingiz qabul qilindi.")
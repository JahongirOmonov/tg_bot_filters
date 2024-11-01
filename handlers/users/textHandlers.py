from aiogram import types
from loader import dp
from aiogram.dispatcher.filters import Text

@dp.message_handler(Text(contains='salom'))
async def bot_text(message: types.Message):
    await message.answer(f"Voleykum salam, {message.from_user.full_name}!")


from aiogram import types
from aiogram.dispatcher import filters
from loader import dp

superuser = 6956376313
# @dp.message_handler(filters.IDFilter(superuser))
@dp.message_handler(chat_id=superuser, commands="start")
async def bot_id(message: types.Message):
    await message.answer(f"ID: {message.from_user.id}")


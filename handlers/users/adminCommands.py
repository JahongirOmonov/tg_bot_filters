from aiogram import types
from loader import dp


@dp.message_handler(commands='falaq', is_chat_admin=True)
async def bot_admin(message: types.Message):
    await message.answer(
        f"Admin: {message.chat.username}"
    )
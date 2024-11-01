from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from loader import dp


# @dp.message_handler(Command("test"))
# async def bot_help(message: types.Message):
#     await message.answer("Test command")


@dp.message_handler(commands=["til"])
async def bot_lan(message: types.Message):
    await message.answer(
        "Tilni tanlang: uz en ru", parse_mode="HTML"
    )
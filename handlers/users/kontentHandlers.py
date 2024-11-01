from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp

@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def dokument(message: types.Message):
    await message.answer(f"Dokumentingiz qabul qilindi!")


@dp.message_handler(content_types='voice')
async def audio(message: types.Message):
    await message.answer(f"Voice qabul qilindi!")

@dp.message_handler(content_types='photo')
@dp.message_handler(content_types=types.ContentType.VIDEO)
async def photo_video(message: types.Message):
    if message.content_type == 'photo':
        await message.answer(f"Foto qabul qilindi {message.chat.id}")
    elif message.content_type == 'video':
        await message.answer(f"video qabul qilindi!")


@dp.message_handler(content_types=types.ContentType.STICKER)
async def sticker(message: types.Message):
    await message.answer(f"Sticker qabul qilindi!")


from aiogram import types
from loader import dp


@dp.message_handler(content_types=types.message.ContentTypes.CONTACT, is_sender_contact=True)
async def bot_contact(message: types.Message):
    print(message)
    await message.answer(
        f"Contact: {message.contact.phone_number}"
    )

@dp.message_handler(commands='kuyov', is_forwarded=True)
async def bot_kuyov(message: types.Message):
    await message.answer(
        f"Kuyov: {message.forward_from.username}"
    )


@dp.message_handler(commands='good', is_reply=True)
async def bot_good(message: types.Message):
    await message.reply(
        f"Good: {message.reply_to_message.text}" #qaysi xabarga reply qilingan bolsa, shu xabarni ushlaydi.
    )
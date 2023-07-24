from src.loader import dp
from aiogram.dispatcher.filters import CommandStart
from aiogram import types

from src.keyboards.inline.lang import long_buttons


@dp.message_handler(CommandStart())
async def send_start(msg: types.Message):
    first_name = msg.from_user.first_name
    await msg.answer(f'Assalomu alaykum <b>{first_name}</b>')

from src.loader import dp

from aiogram.filters import CommandStart
from aiogram import types
from aiogram.utils.markdown import hbold


@dp.message(CommandStart())
async def send_start(message: types.Message):
    first_name = message.from_user.first_name
    await message.answer(f'Assalomu alaykum {hbold(first_name)}!')

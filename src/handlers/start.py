from ..loader import dp
from aiogram.dispatcher.filters import CommandStart
from aiogram import types

from ..keyboards.inline.lang import long_buttons


@dp.message_handler(CommandStart())
async def send_start(msg: types.Message):
    first_name = msg.from_user.first_name
    await msg.answer(f'  🇺🇿 Assalomu alaykum <b>{first_name}</b> iPro group rasmiy botiga Xush Kelibsiz\n\n'
                     f'🇷🇺 Здравствуйте и добро пожаловать в официальный бот группы iPro <b>{first_name}</b>\n\n'
                     f'<b>Tilni tanlang</b>\n<b>Выберите язык</b>',
                     reply_markup=long_buttons)

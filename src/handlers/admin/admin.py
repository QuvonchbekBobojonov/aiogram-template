from src.loader import dp
from aiogram.dispatcher.filters import Command
from aiogram import types

from src.config import ADMINS

from src.keyboards.default.admin.admin_panel import admin_btns


@dp.message_handler(Command('admin'))
async def send_start(msg: types.Message):
    if str(msg.from_user.id) in ADMINS:
        await msg.answer('Admin panel', reply_markup=admin_btns)

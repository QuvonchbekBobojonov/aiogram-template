import logging

from aiogram import Bot

from src.db.models.users import User


async def on_startup_notify(bot: Bot):
    """Notify admins about successful start"""
    for admin in User.get_admins():
        try:
            await bot.send_message(
                admin.id,
                "Бот Запущен и готов к работе!",
            )
        except Exception as err:
            logging.exception(err)

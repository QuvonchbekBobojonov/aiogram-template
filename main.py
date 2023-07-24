from aiogram import executor

from src.loader import dp

import src.handlers

from src.utils import set_default_commands, on_startup_notify


async def on_startup(dispatcher):
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

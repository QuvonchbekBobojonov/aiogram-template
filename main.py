import logging
import asyncio

from src.loader import dp, bot

import src.handlers

from src.utils import set_default_commands, on_startup_notify


async def main():
    await set_default_commands(bot)
    await on_startup_notify(dp)
    await dp.start_polling(bot, skip_updates=True)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

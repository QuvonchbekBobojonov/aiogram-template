from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode

from .settings import BOT_TOKEN
from .db.models.base import BaseModel, get_db

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

# connect to database
db = get_db()
db.connect()
db.create_tables(BaseModel.__subclasses__())
db.close()

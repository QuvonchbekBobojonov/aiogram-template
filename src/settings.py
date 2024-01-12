from environs import Env
from src.db import DatabaseConnection, DatabaseTypes
import pytz

# read .env file
env = Env()
env.read_env()

# bot token from @BotFather
BOT_TOKEN = env.str('BOT_TOKEN')

# admins id
# ADMINS = env.list('ADMINS')


# database connection
# database types (postgresql, sqlite)
database = DatabaseConnection(
    db_type=DatabaseTypes.SQLITE,
)

# time zone
TIMEZONE = pytz.timezone('Asia/Tashkent')

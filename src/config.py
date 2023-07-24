from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str('BOT_TOKEN')

DATABASE_URL = env.str('DATABASE_URL')

ADMINS = env.list('ADMINS')

from abc import ABC
from datetime import datetime
from aiogram import BaseMiddleware, types

from src.settings import TIMEZONE

from src.db.models.users import User

datetime_now = datetime.now(TIMEZONE)


class AuthMiddleware(BaseMiddleware, ABC):
    @staticmethod
    async def __call__(message: types.Message, *args, **kwargs):
        if message.from_user.is_bot:
            return
        user, created = User.get_or_create(
            id=message.from_user.id,
            defaults={
                'username': message.from_user.username,
                'first_name': message.from_user.first_name,
                'last_name': message.from_user.last_name,
                'language_code': message.from_user.language_code,
                'is_bot': message.from_user.is_bot,
                'created_at': datetime_now,
                'updated_at': datetime_now,
                'deleted_at': None,
                'is_active': True,
                'is_admin': False,
            }
        )
        message.from_user = user
        return


import peewee
from src.db.models.base import BaseModel


class User(BaseModel):
    id = peewee.IntegerField(unique=True, primary_key=True)
    username = peewee.CharField(max_length=255, null=True)
    first_name = peewee.CharField(max_length=255, null=True)
    last_name = peewee.CharField(max_length=255, null=True)
    language_code = peewee.CharField(max_length=10, null=True)
    is_bot = peewee.BooleanField(default=False)
    created_at = peewee.DateTimeField(null=True)
    updated_at = peewee.DateTimeField(null=True)
    deleted_at = peewee.DateTimeField(null=True)
    is_active = peewee.BooleanField(default=True)
    is_admin = peewee.BooleanField(default=False)

    class Meta:
        db_table = 'users'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_letter_name(self):
        return f'{self.first_name} {self.last_name[0]}.'

    @classmethod
    def get_admins(cls):
        return cls.get_or_none(is_admin=True) or []

    def __str__(self):
        return self.get_full_name()

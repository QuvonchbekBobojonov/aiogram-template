import peewee

from src.db import DatabaseTypes, DatabaseConnectionError
from src.settings import database


def get_db():
    if database.db_type == DatabaseTypes.POSTGRESQL:
        db = peewee.PostgresqlDatabase(
            database.db_name,
            user=database.db_user,
            password=database.db_password,
            host=database.db_host,
            port=database.db_port
        )
    elif database.db_type == DatabaseTypes.SQLITE:
        db = peewee.SqliteDatabase('db.sqlite3')

    else:
        raise DatabaseConnectionError('Unknown database type')

    return db


class BaseModel(peewee.Model):

    class Meta:
        database = get_db()

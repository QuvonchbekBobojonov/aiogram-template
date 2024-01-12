from enum import Enum


class DatabaseConnection:
    def __init__(self, db_type, db_name=None, db_user=None, db_password=None, db_host=None, db_port=None):
        self.db_type = db_type
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password
        self.db_host = db_host
        self.db_port = db_port


class DatabaseTypes(Enum):
    POSTGRESQL = 'postgresql'
    SQLITE = 'sqlite'


class DatabaseConnectionError(Exception):
    pass

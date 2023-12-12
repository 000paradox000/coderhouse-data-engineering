import psycopg2

from .db_manager import DBManager


class PostgreSQLManager(DBManager):
    @property
    def _params(self):
        return {
            'host': 'db_postgres',
            'port': '5432',
            'database': 'coderhouse',
            'user': 'coderhouse',
            'password': 'coderhouse'
        }

    def _connect(self):
        self._conn = psycopg2.connect(**self._params)

import mysql.connector

from .db_manager import DBManager


class MySQLManager(DBManager):
    @property
    def _params(self):
        return {
            'host': 'db_mysql',
            'port': '3306',
            'database': 'coderhouse',
            'user': 'coderhouse',
            'password': 'coderhouse'
        }

    def _connect(self):
        self._conn = mysql.connector.connect(**self._params)

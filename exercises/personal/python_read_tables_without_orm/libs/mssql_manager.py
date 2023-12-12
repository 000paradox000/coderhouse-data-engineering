import pymssql

from .db_manager import DBManager


class MSSQLManager(DBManager):
    @property
    def _params(self):
        return {
            'server': 'db_mssql',
            'port': '1433',
            'database': 'coderhouse',
            'user': 'coderhouse',
            'password': 'C0d3rhous3'
        }

    def _connect(self):
        self._conn = pymssql.connect(**self._params)

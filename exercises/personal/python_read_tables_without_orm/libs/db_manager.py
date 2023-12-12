from tabulate import tabulate


class DBManager:
    def __init__(self):
        self._conn = None
        self._cursor = None

    @property
    def _params(self):
        raise NotImplementedError

    def _connect(self):
        raise NotImplementedError

    def _disconnect(self):
        self._conn.close()

    def query_table(self, table_name, limit=None):
        if limit is None:
            sql = f"SELECT * FROM {table_name}"
        else:
            sql = f"SELECT * FROM {table_name} LIMIT {limit}"

        self._cursor.execute(sql)
        rows = self._cursor.fetchall()

        return rows

    @staticmethod
    def print_rows(rows):
        print(tabulate(rows))

    def __enter__(self):
        self._connect()
        self._cursor = self._conn.cursor()

        return self

    def __exit__(self, *args):
        self._cursor.close()
        self._disconnect()

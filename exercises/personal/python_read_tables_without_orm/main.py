"""
Reading tables from some databases without an ORM
"""

from libs.postgres_manager import PostgreSQLManager
from libs.mysql_manager import MySQLManager
from libs.mssql_manager import MSSQLManager


def main():
    tables = [
        ["Agents", "agents"],
        ["Customers", "customers"],
        ["Calls", "calls"],
    ]
    managers = [
        ["PostgreSQL", PostgreSQLManager],
        ["MySQL", MySQLManager],
        ["MySQL", MySQLManager],
        ["MSSQL", MSSQLManager],
    ]

    for manager_name, manager_cls in managers:
        print("")
        print(manager_name)
        print("=" * 50)
        with manager_cls() as manager:
            for title, name in tables:
                print("")
                print(title)
                print("-" * 50)
                rows = manager.query_table(name)
                manager.print_rows(rows)
        print("")


if __name__ == '__main__':
    main()

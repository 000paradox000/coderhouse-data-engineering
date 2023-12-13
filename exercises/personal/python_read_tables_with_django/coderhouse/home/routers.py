from .models import AgentPostgres
from .models import AgentMySQL
from .models import AgentMSSQL

from .models import CustomerPostgres
from .models import CustomerMySQL
from .models import CustomerMSSQL

from .models import CallPostgres
from .models import CallMySQL
from .models import CallMSSQL


class DBPostgresRouter:
    def db_for_read(self, model, **hints):
        if model in [AgentPostgres, CustomerPostgres, CallPostgres]:
            return 'db_postgres'
        return None


class DBMySQLRouter:
    def db_for_read(self, model, **hints):
        if model in [AgentMySQL, CustomerMySQL, CallMySQL]:
            return 'db_mysql'
        return None


class DBMSSQLRouter:
    def db_for_read(self, model, **hints):
        if model in [AgentMSSQL, CustomerMSSQL, CallMSSQL]:
            return 'db_mssql'
        return None

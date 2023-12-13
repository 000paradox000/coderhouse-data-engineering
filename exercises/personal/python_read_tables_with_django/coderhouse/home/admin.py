from django.contrib import admin

from .models import AgentPostgres
from .models import AgentMySQL
from .models import AgentMSSQL

from .models import CustomerPostgres
from .models import CustomerMySQL
from .models import CustomerMSSQL

from .models import CallPostgres
from .models import CallMySQL
from .models import CallMSSQL


class ReadOnlyAdmin:
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


class AgentAdmin(ReadOnlyAdmin, admin.ModelAdmin):
    list_display = [
        "agentid",
        "name",
    ]


@admin.register(AgentPostgres)
class AgentPostgresAdmin(AgentAdmin):
    pass


@admin.register(AgentMySQL)
class AgentMySQLAdmin(AgentAdmin):
    pass


@admin.register(AgentMSSQL)
class AgentMSSQLAdmin(AgentAdmin):
    pass


class CustomerAdmin(ReadOnlyAdmin, admin.ModelAdmin):
    list_display = [
        "customerid",
        "name",
        "occupation",
        "email",
        "company",
        "phonenumber",
        "age",
    ]


@admin.register(CustomerPostgres)
class CustomerPostgresAdmin(CustomerAdmin):
    pass


@admin.register(CustomerMySQL)
class CustomerMySQLAdmin(CustomerAdmin):
    pass


@admin.register(CustomerMSSQL)
class CustomerMSSQLAdmin(CustomerAdmin):
    pass


class CallAdmin(ReadOnlyAdmin, admin.ModelAdmin):
    list_display = [
        "callid",
        "agentid",
        "customerid",
        "pickedup",
        "duration",
        "productsold",
    ]


@admin.register(CallPostgres)
class CallPostgresAdmin(CallAdmin):
    pass


@admin.register(CallMySQL)
class CallMySQLAdmin(CallAdmin):
    pass


@admin.register(CallMSSQL)
class CallMSSQLAdmin(CallAdmin):
    pass

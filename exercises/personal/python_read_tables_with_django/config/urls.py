from django.contrib import admin
from django.urls import path, reverse_lazy
from django.views.generic.base import RedirectView

from coderhouse.home.views import (
    AgentPostgresListCreateView,
    AgentMySQLListCreateView,
    AgentMSSQLListCreateView,
    CustomerPostgresListCreateView,
    CustomerMySQLListCreateView,
    CustomerMSSQLListCreateView,
    CallPostgresListCreateView,
    CallMySQLListCreateView,
    CallMSSQLListCreateView,
)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('agents/postgres/', 
         AgentPostgresListCreateView.as_view(), name='agents_postgres'),
    path('agents/mysql/', 
         AgentMySQLListCreateView.as_view(), name='agents_mysql'),
    path('agents/mssql/', 
         AgentMSSQLListCreateView.as_view(), name='agents_mssql'),

    path('customers/postgres/',
         CustomerPostgresListCreateView.as_view(), name='customers_postgres'),
    path('customers/mysql/',
         CustomerMySQLListCreateView.as_view(), name='customers_mysql'),
    path('customers/mssql/',
         CustomerMSSQLListCreateView.as_view(), name='customers_mssql'),

    path('calls/postgres/',
         CallPostgresListCreateView.as_view(), name='calls_postgres'),
    path('calls/mysql/',
         CallMySQLListCreateView.as_view(), name='calls_mysql'),
    path('calls/mssql/',
         CallMSSQLListCreateView.as_view(), name='calls_mssql'),

    path('', RedirectView.as_view(url=reverse_lazy("admin:index"),
                                  permanent=True)),
]

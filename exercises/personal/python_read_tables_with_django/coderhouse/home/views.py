from rest_framework import generics

from .models import (
    AgentPostgres,
    AgentMySQL,
    AgentMSSQL,
    CustomerPostgres,
    CustomerMySQL,
    CustomerMSSQL,
    CallPostgres,
    CallMySQL,
    CallMSSQL,
)

from .serializers import (
    AgentPostgresSerializer, 
    AgentMySQLSerializer, 
    AgentMSSQLSerializer,
    CustomerPostgresSerializer,
    CustomerMySQLSerializer,
    CustomerMSSQLSerializer,
    CallPostgresSerializer,
    CallMySQLSerializer,
    CallMSSQLSerializer,
)


class AgentPostgresListCreateView(generics.ListCreateAPIView):
    queryset = AgentPostgres.objects.all()
    serializer_class = AgentPostgresSerializer


class AgentMySQLListCreateView(generics.ListCreateAPIView):
    queryset = AgentMySQL.objects.all()
    serializer_class = AgentMySQLSerializer


class AgentMSSQLListCreateView(generics.ListCreateAPIView):
    queryset = AgentMSSQL.objects.all()
    serializer_class = AgentMSSQLSerializer


class CustomerPostgresListCreateView(generics.ListCreateAPIView):
    queryset = CustomerPostgres.objects.all()
    serializer_class = CustomerPostgresSerializer


class CustomerMySQLListCreateView(generics.ListCreateAPIView):
    queryset = CustomerMySQL.objects.all()
    serializer_class = CustomerMySQLSerializer


class CustomerMSSQLListCreateView(generics.ListCreateAPIView):
    queryset = CustomerMSSQL.objects.all()
    serializer_class = CustomerMSSQLSerializer


class CallPostgresListCreateView(generics.ListCreateAPIView):
    queryset = CallPostgres.objects.all()
    serializer_class = CallPostgresSerializer


class CallMySQLListCreateView(generics.ListCreateAPIView):
    queryset = CallMySQL.objects.all()
    serializer_class = CallMySQLSerializer


class CallMSSQLListCreateView(generics.ListCreateAPIView):
    queryset = CallMSSQL.objects.all()
    serializer_class = CallMSSQLSerializer

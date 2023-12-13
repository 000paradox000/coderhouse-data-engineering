from rest_framework import serializers

from .models import AgentPostgres, AgentMySQL, AgentMSSQL
from .models import CustomerPostgres, CustomerMySQL, CustomerMSSQL
from .models import CallPostgres, CallMySQL, CallMSSQL


class AgentPostgresSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentPostgres
        fields = '__all__'


class AgentMySQLSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentMySQL
        fields = '__all__'


class AgentMSSQLSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentMSSQL
        fields = '__all__'


class CustomerPostgresSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerPostgres
        fields = '__all__'


class CustomerMySQLSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerMySQL
        fields = '__all__'


class CustomerMSSQLSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerMSSQL
        fields = '__all__'


class CallPostgresSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallPostgres
        fields = '__all__'


class CallMySQLSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallMySQL
        fields = '__all__'


class CallMSSQLSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallMSSQL
        fields = '__all__'

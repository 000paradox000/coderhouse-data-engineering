from django.db import models


class Agent(models.Model):
    agentid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    def save(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        db_table = 'agents'
        managed = False


class AgentPostgres(Agent):
    class Meta(Agent.Meta):
        verbose_name = "Agent Postgres"
        verbose_name_plural = "Agent Postgres"


class AgentMySQL(Agent):
    class Meta(Agent.Meta):
        verbose_name = "Agent MySQL"
        verbose_name_plural = "Agent MySQL"


class AgentMSSQL(Agent):
    class Meta(Agent.Meta):
        verbose_name = "Agent MSSQL"
        verbose_name_plural = "Agent MSSQL"


class Customer(models.Model):
    customerid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    occupation = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    company = models.CharField(max_length=50, blank=True, null=True)
    phonenumber = models.CharField(max_length=20, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        db_table = 'customers'
        managed = False


class CustomerPostgres(Customer):
    class Meta(Customer.Meta):
        verbose_name = "Customer Postgres"
        verbose_name_plural = "Customer Postgres"


class CustomerMySQL(Customer):
    class Meta(Customer.Meta):
        verbose_name = "Customer MySQL"
        verbose_name_plural = "Customer MySQL"


class CustomerMSSQL(Customer):
    class Meta(Customer.Meta):
        verbose_name = "Customer MSSQL"
        verbose_name_plural = "Customer MSSQL"


class Call(models.Model):
    callid = models.IntegerField(primary_key=True)
    agentid = models.IntegerField(blank=True, null=True)
    customerid = models.IntegerField(blank=True, null=True)
    pickedup = models.SmallIntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    productsold = models.SmallIntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass

    def __str__(self):
        return f"{self.callid}"

    class Meta:
        abstract = True
        db_table = 'calls'
        managed = False


class CallPostgres(Call):
    class Meta(Call.Meta):
        verbose_name = "Call Postgres"
        verbose_name_plural = "Call Postgres"


class CallMySQL(Call):
    class Meta(Call.Meta):
        verbose_name = "Call MySQL"
        verbose_name_plural = "Call MySQL"


class CallMSSQL(Call):
    class Meta(Call.Meta):
        verbose_name = "Call MSSQL"
        verbose_name_plural = "Call MSSQL"

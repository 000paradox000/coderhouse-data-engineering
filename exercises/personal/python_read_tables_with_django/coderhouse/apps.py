from django.contrib.admin.apps import AdminConfig


class CoderHouseConfig(AdminConfig):
    default_site = "coderhouse.admin.CoderHouseAdminSite"

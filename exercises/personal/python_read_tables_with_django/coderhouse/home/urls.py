from django.urls import path

from .views.home import Home
from .views.update_date_setting import UpdateDateSetting
from .views.update_order_setting import UpdateOrderSetting
from .views.download_certificate import DownloadCertificate

app_name = "home"

urlpatterns = [
    path("", Home.as_view(), name="index"),
    path(
        "update/date", UpdateDateSetting.as_view(), name="update_date_setting"
    ),
    path(
        "update/order",
        UpdateOrderSetting.as_view(),
        name="update_order_setting",
    ),
    path(
        "download/<int:pk>",
        DownloadCertificate.as_view(),
        name="download_certificate",
    ),
]

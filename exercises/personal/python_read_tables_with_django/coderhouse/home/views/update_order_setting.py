from django.urls import reverse_lazy

from .base import UpdateSetting
from alpha_editorial_certificates.certificates.models import OrderSettings
from alpha_editorial_certificates.certificates.forms.settings import (
    OrderSettingsForm,
)
from alpha_editorial_certificates.certificates.layouts.order_setting import (
    OrderSettingLayout,
)


class UpdateOrderSetting(UpdateSetting):
    model = OrderSettings
    success_message = "Orden actualizado exitosamente"
    title = "Actualizar orden"
    action_url = reverse_lazy("home:update_order_setting")
    form_class = OrderSettingsForm
    layout = OrderSettingLayout()

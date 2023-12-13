from django.urls import reverse_lazy

from .base import UpdateSetting
from alpha_editorial_certificates.certificates.models import DateSettings
from alpha_editorial_certificates.certificates.forms.settings import (
    DateSettingsForm,
)
from alpha_editorial_certificates.certificates.layouts.date_setting import (
    DateSettingLayout,
)


class UpdateDateSetting(UpdateSetting):
    model = DateSettings
    success_message = "Rango de fechas actualizado exitosamente"
    title = "Actualizar rango de fechas"
    action_url = reverse_lazy("home:update_date_setting")
    form_class = DateSettingsForm
    layout = DateSettingLayout()

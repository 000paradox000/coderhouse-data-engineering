from django.views.generic import ListView

from alpha_editorial_certificates.users.mixins.check_authenticated_redirect_to_login import (
    CheckAuthenticatedRedirectToLogin,
)
from alpha_editorial_certificates.certificates.models import Certificate
from alpha_editorial_certificates.certificates.models import DateSettings
from alpha_editorial_certificates.certificates.models import OrderSettings


class Home(CheckAuthenticatedRedirectToLogin, ListView):
    template_name = "home/index.html"
    model = Certificate
    context_object_name = "certificates"
    _date_setting = None
    _order_setting = None

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(
            object_list=object_list, **kwargs
        )

        context_data.update(
            {
                "order_setting": self.order_setting,
                "date_setting": self.date_setting,
            }
        )

        return context_data

    def get_queryset(self):
        return (
            super(Home, self)
            .get_queryset()
            .get_certificates_for_user(self.request)
        )

    @property
    def date_setting(self):
        if self._date_setting is None:
            self._date_setting = DateSettings.objects.get_setting_for_user(
                self.request
            )

        return self._date_setting

    @property
    def order_setting(self):
        if self._order_setting is None:
            self._order_setting = OrderSettings.objects.get_setting_for_user(
                self.request
            )

        return self._order_setting

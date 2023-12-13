from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.contrib import messages

from alpha_editorial_certificates.users.mixins.check_authenticated import (
    CheckAuthenticated,
)
from alpha_editorial_certificates.common import utilities


class UpdateSetting(CheckAuthenticated, UpdateView):
    success_url = reverse_lazy("home:index")
    template_name = "home/update-setting.html"
    success_message = None
    title = None
    action_url = None
    layout = None

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        context_data.update(
            {
                "title": self.title,
                "action_url": self.action_url,
                "layout": self.layout,
            }
        )

        return context_data

    def form_valid(self, form):
        setting = form.save(commit=False)
        setting.modification_user = self.request.user
        setting.modification_ip = utilities.get_visitor_ip(self.request)
        setting.save()

        if self.success_message:
            messages.success(self.request, self.success_message)
        return super().form_valid(form)

    def get_object(self, queryset=None):
        if queryset is not None:
            return queryset.get_setting_for_user(self.request)

        return self.model.objects.get_setting_for_user(self.request)

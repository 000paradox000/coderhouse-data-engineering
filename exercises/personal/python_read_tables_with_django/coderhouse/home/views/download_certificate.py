import os

from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.http import HttpResponse

from alpha_editorial_certificates.users.mixins.check_authenticated import (
    CheckAuthenticated,
)
from alpha_editorial_certificates.certificates.models import Certificate
from alpha_editorial_certificates.certificates.models import Download
from alpha_editorial_certificates.common import utilities


class DownloadCertificate(CheckAuthenticated, DetailView):
    success_url = reverse_lazy("home:index")
    template_name = "common/dummy.html"
    model = Certificate

    def get_queryset(self):
        return super().get_queryset().get_certificates_for_user(self.request)

    def render_to_response(self, context, **response_kwargs):
        obj = self.object
        Download.objects.create(
            certificate=obj,
            user=self.request.user,
            creation_user=self.request.user,
            modification_user=self.request.user,
            creation_ip=utilities.get_visitor_ip(self.request),
            modification_ip=utilities.get_visitor_ip(self.request),
        )
        path = obj.uploaded_file.path
        _, full_extension = os.path.splitext(path)
        extension = full_extension[1:]
        response = HttpResponse(content_type=f"application/{extension}")
        file_name = f"{utilities.generate_unique_name()}{full_extension}"
        response["Content-Disposition"] = f'attachment; filename="{file_name}"'
        response.write(open(path, "rb").read())

        return response

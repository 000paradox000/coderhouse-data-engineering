from django.contrib import admin
from django.urls import path, reverse_lazy
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy("admin:index"), permanent=True)),
    path('admin/', admin.site.urls),
]

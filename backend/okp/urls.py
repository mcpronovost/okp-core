"""
URL configuration.
"""
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path

from .views import OkpTemplateView


urlpatterns = [
    path("admin/", admin.site.urls),
    # api
    path("api/", include("okp.api.urls")),
] + i18n_patterns(
    # app
    re_path(r"^", OkpTemplateView.as_view(template_name="index.html")),
    # path("<path:path>", OkpTemplateView.as_view(template_name="index.html")),
)

urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
)
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
